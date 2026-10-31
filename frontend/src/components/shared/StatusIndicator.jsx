import React from 'react';

export default function StatusIndicator({ isOnline = true, ollamaReady = false }) {
  return (
    <div style={{ display: 'flex', gap: '0.75rem', fontSize: '0.85rem', color: '#475569' }}>
      <span>Backend: {isOnline ? '🟢 Connected (127.0.0.1:8000)' : '🔴 Offline'}</span>
      <span>Ollama (Llama 3.2): {ollamaReady ? '🟢 Ready' : '⚪ Unchecked'}</span>
    </div>
  );
}
