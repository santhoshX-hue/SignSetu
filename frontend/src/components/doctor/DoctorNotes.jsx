import React from 'react';

/**
 * Doctor notes input panel.
 * Doctor writes explanations to be simplified for the patient.
 */
export default function DoctorNotes() {
  return (
    <section style={{ background: '#fff', padding: '1rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3>Doctor Notes & Clinical Explanation</h3>
      <p style={{ color: '#64748b', fontSize: '0.9rem' }}>
        Input doctor clinical explanation for plain-language simplification. (UI logic to be implemented).
      </p>
    </section>
  );
}
