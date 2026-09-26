// src/pages/AuditLogsPage.jsx
// Shows the system-wide audit log (all tickets), newest first.
// Read-only — no create/update/delete, matching the backend design.
import { useEffect, useState } from 'react'
import { getAllAuditLogs } from '../api/client'

export default function AuditLogsPage() {
  const [logs, setLogs] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    getAllAuditLogs()
      .then(setLogs)
      .catch((err) => setError(err.message || 'Could not load audit logs.'))
      .finally(() => setLoading(false))
  }, [])

  const shortId = (value) => {
    if (typeof value !== 'string' || !value) return '—'
    return value.length > 8 ? `${value.slice(0, 8)}…` : value
  }

  return (
    <div>
      <h4>Audit Logs <small className="text-muted fs-6">(all tickets, newest first)</small></h4>

      {loading ? <p>Loading audit logs…</p> : error ? (
        <div className="alert alert-danger" role="alert">Unable to load audit logs: {error}</div>
      ) : (
        <table className="table table-sm table-bordered">
          <thead className="table-dark">
            <tr><th>Action</th><th>Ticket ID</th><th>Performed By</th><th>Details</th><th>When</th></tr>
          </thead>
          <tbody>
            {logs.length === 0 && <tr><td colSpan={5} className="text-center text-muted">No audit log entries yet.</td></tr>}
            {logs.map(log => (
              <tr key={log.id}>
                <td><span className="badge bg-info text-dark">{log.action}</span></td>
                <td><code>{shortId(log.ticket_id)}</code></td>
                <td><code>{shortId(log.performed_by)}</code></td>
                <td>{log.details}</td>
                <td><small>{log.created_at ? new Date(log.created_at).toLocaleString() : '—'}</small></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}