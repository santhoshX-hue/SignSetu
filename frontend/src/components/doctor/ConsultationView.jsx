import React from 'react';
import DoctorNotes from './DoctorNotes';
import SimplifiedOutput from './SimplifiedOutput';

/**
 * Doctor Consultation Container.
 * Brings together doctor notes input, live transcription view, and simplification review.
 */
export default function ConsultationView() {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
      <DoctorNotes />
      <SimplifiedOutput />
    </div>
  );
}
