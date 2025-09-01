import React, { useState } from 'react';
import './App.css';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  const [mode, setMode] = useState('login'); // 'login' | 'register'
  const [user, setUser] = useState(null);

  if (user) {
    return (
      <div className="App">
        <header className="App-header">
          <h2>Welcome {user.displayName || user.email}</h2>
          <p>You are logged in.</p>
        </header>
      </div>
    );
  }

  return (
    <div className="App">
      {mode === 'login' ? (
        <Login onSwitchToRegister={() => setMode('register')} onLoginSuccess={setUser} />
      ) : (
        <Register onSwitchToLogin={() => setMode('login')} onRegisterSuccess={setUser} />
      )}
    </div>
  );
}

export default App;
