import React from 'react';

/**
 * AI-Simplified Draft Review Panel.
 *
 * Mandatory Workflow Rule:
 * Requires explicit doctor review and approval before any response
 * is transmitted to the patient or converted to ISL.
 */
export default function SimplifiedOutput() {
  return (
    <section style={{ background: '#fff', padding: '1rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3>AI-Simplified Explanation (Pending Doctor Review)</h3>
      <p style={{ color: '#64748b', fontSize: '0.9rem' }}>
        Doctor must inspect and approve this draft before dispatch. (UI logic to be implemented).
      </p>
    </section>
  );
}
