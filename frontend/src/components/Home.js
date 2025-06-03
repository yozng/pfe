/*import React from 'react'

const Home = () => {
  return (
    <div>Home</div>
  )
}

export default Home */
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      {/* En-tête */}
      <header className="hero-section">
        <div className="hero-content">
          <h1>Bienvenue sur la Plateforme Doctorale de la Faculté</h1>
          <p>Un espace dédié au suivi et à la gestion de votre parcours doctoral</p>
        </div>
      </header>

      {/* Section d'authentification */}
      <section className="auth-section">
        <div className="auth-tabs">
          <div className="auth-card" onClick={() => navigate('/login/student')}>
            <div className="auth-icon">
              <i className="fas fa-user-graduate"></i>
            </div>
            <h3>Doctorant</h3>
            <p>Accédez à votre espace personnel pour gérer votre parcours doctoral</p>
            <div className="auth-actions">
              <button className="btn-primary">Connexion</button>
              <button className="btn-secondary" onClick={(e) => { e.stopPropagation(); navigate('/register/student'); }}>
                Inscription
              </button>
            </div>
          </div>

          <div className="auth-card" onClick={() => navigate('/login/advisor')}>
            <div className="auth-icon">
              <i className="fas fa-chalkboard-teacher"></i>
            </div>
            <h3>Encadrant</h3>
            <p>Espace dédié au suivi des doctorants et validation des demandes</p>
            <div className="auth-actions">
              <button className="btn-primary">Connexion</button>
            </div>
          </div>

          <div className="auth-card" onClick={() => navigate('/login/admin')}>
            <div className="auth-icon">
              <i className="fas fa-user-shield"></i>
            </div>
            <h3>Administrateur</h3>
            <p>Interface de gestion des utilisateurs et des thèses</p>
            <div className="auth-actions">
              <button className="btn-primary">Connexion</button>
            </div>
          </div>
        </div>
      </section>

      {/* Section fonctionnalités */}
      <section className="features-section">
        <h2>Nos Fonctionnalités</h2>
        <div className="features-grid">
          <div className="feature-card">
            <i className="fas fa-file-upload"></i>
            <h3>Soumission en ligne</h3>
            <p>Déposez vos demandes de dérogation, soutenance et documents académiques</p>
          </div>
          <div className="feature-card">
            <i className="fas fa-chart-line"></i>
            <h3>Suivi en temps réel</h3>
            <p>Visualisez l'état d'avancement de vos demandes et de votre parcours</p>
          </div>
          <div className="feature-card">
            <i className="fas fa-book"></i>
            <h3>Archivage des thèses</h3>
            <p>Accédez à l'ensemble des thèses soutenues dans notre bibliothèque numérique</p>
          </div>
          <div className="feature-card">
            <i className="fas fa-chart-pie"></i>
            <h3>Tableaux de bord</h3>
            <p>Analysez vos performances et statistiques académiques</p>
          </div>
        </div>
      </section>

      {/* Pied de page */}
      <footer className="home-footer">
        <p>© 2024 Plateforme Doctorale - Faculté des Sciences</p>
        <div className="footer-links">
          <a href="/about">À propos</a>
          <a href="/contact">Contact</a>
          <a href="/help">Aide</a>
        </div>
      </footer>
    </div>
  );
};

export default Home;