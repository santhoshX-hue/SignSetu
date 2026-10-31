import React from 'react';

export default function Navbar({ activeTab, setActiveTab }) {
  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.75rem 1.5rem', background: '#0f172a', color: '#fff' }}>
      <div style={{ fontWeight: 'bold', fontSize: '1.25rem' }}>SignSetu</div>
      <nav style={{ display: 'flex', gap: '1rem' }}>
        <button
          onClick={() => setActiveTab('doctor')}
          style={{
            background: activeTab === 'doctor' ? '#2563eb' : 'transparent',
            color: '#fff',
            border: 'none',
            padding: '0.5rem 1rem',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Doctor Dashboard
        </button>
        <button
          onClick={() => setActiveTab('patient')}
          style={{
            background: activeTab === 'patient' ? '#2563eb' : 'transparent',
            color: '#fff',
            border: 'none',
            padding: '0.5rem 1rem',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Patient View (Teammate)
        </button>
      </nav>
    </header>
  );
}
