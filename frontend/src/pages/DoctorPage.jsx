import React from 'react';
import ConsultationView from '../components/doctor/ConsultationView';
import StatusIndicator from '../components/shared/StatusIndicator';

export default function DoctorPage() {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Doctor Consultation Dashboard</h2>
        <StatusIndicator />
      </div>
      <ConsultationView />
    </div>
  );
}
