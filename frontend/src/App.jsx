import React, { useState } from 'react';
import Navbar from './components/shared/Navbar';
import DoctorPage from './pages/DoctorPage';
import PatientPage from './pages/PatientPage';

/**
 * SHARED INTEGRATION FILE: Top-level view switcher.
 * Provides views for both Doctor Dashboard and Patient Dashboard.
 */
export default function App() {
  const [activeTab, setActiveTab] = useState('doctor');

  return (
    <div style={{ minHeight: '100vh', fontFamily: 'sans-serif', backgroundColor: '#f8fafc' }}>
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />
      <main style={{ padding: '1rem' }}>
        {activeTab === 'doctor' ? <DoctorPage /> : <PatientPage />}
      </main>
    </div>
  );
}
