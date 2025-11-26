# CogniSync - GenAI-Powered Music Therapy Platform

Empowering recovery through AI-personalized rhythmic therapy and real-time adaptation.

## Overview

CogniSync is a clinical-grade neurorehabilitation platform that uses AI-driven rhythmic therapy to help patients with Parkinson's disease and stroke recovery. The system uses auditory-motor entrainment principles, where patients synchronize movements to personalized beats to bypass damaged neural pathways and improve motor control, gait, speech, and fine motor skills.

## Key Features

- **Personalized Therapy**: AI-adapted rhythmic therapy tailored to individual patient capabilities
- **Real-time Adaptation**: Dynamic tempo adjustment based on patient performance
- **Complete Clinical Workflow**: Assessment → Prescription → Therapy → Monitoring
- **Progress Tracking**: Detailed analytics and trend visualization for data-driven treatment
- **Multi-modal Training**: Gait training, speech rhythm therapy, and fine motor exercises

## Technology Stack

### Backend
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: SQLite (development) / PostgreSQL (production)
- **Security**: Werkzeug password hashing
- **Session Management**: Flask server-side sessions

### Frontend
- **Template Engine**: Jinja2 with Bootstrap dark theme
- **Audio Processing**: Tone.js for real-time beat generation
- **Visualization**: Chart.js for progress metrics
- **Icons**: Feather Icons

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser with Web Audio API support

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cognisync.git
cd cognisync
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (optional):
```bash
export DATABASE_URL="postgresql://user:password@localhost/cognisync"
export SECRET_KEY="your-secret-key"
```

4. Initialize the database:
```bash
python app.py
```

5. Run the application:
```bash
flask run
```

6. Access the platform at `http://localhost:5000`

## Usage

### For Clinicians

1. **Register** a clinician account
2. **Create patient profiles** with baseline assessments
3. **Prescribe therapy targets** based on assessment results
4. **Monitor progress** through analytics dashboard
5. **Adjust treatment** based on performance data

### For Patients

1. **Log in** with credentials provided by your clinician
2. **Complete baseline assessments** for gait, tapping, and speech
3. **Start therapy sessions** with guided rhythmic exercises
4. **Follow visual and audio cues** to synchronize movements
5. **Track your progress** over time

## Clinical Workflow

### 1. Assessment Phase
Multi-modal baseline testing to establish patient capabilities:
- Gait assessment (steps per minute, stride length)
- Tapping assessment (taps per minute, consistency)
- Speech assessment (syllables per minute, rhythm accuracy)

### 2. Prescription Phase
Clinicians define personalized therapy parameters:
- Target tempo and rhythm patterns
- Session duration and frequency
- Specific exercise types

### 3. Therapy Phase
Interactive sessions with real-time feedback:
- Visual metronome and cue indicators
- Adaptive tempo adjustment
- Performance accuracy tracking

### 4. Monitoring Phase
Comprehensive progress tracking:
- Session history and metrics
- Trend visualization
- Treatment effectiveness analysis

## Architecture

### Data Model
- **Users**: Dual-role system (patients and clinicians)
- **Patient Profiles**: Condition tracking and baseline measurements
- **Sessions**: Therapy data with real-time metrics
- **Assessments**: Baseline capability measurements

### Audio Processing
- Client-side beat generation using Tone.js
- Real-time BPM adjustment based on performance
- Multiple therapy modes with different rhythm patterns

## Configuration

### Database Configuration
The platform supports both SQLite and PostgreSQL:

```python
# Development (SQLite)
DATABASE_URL not set - uses local SQLite database

# Production (PostgreSQL)
DATABASE_URL="postgresql://user:password@host:port/database"
```

### Environment Variables
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: Flask session encryption key
- `FLASK_ENV`: Environment mode (development/production)

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

- All passwords are hashed using Werkzeug's secure hashing
- Server-side session management
- Input validation and sanitization
- Secure database connections with connection pooling

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact:
- Email: support@cognisync.com
- Documentation: https://docs.cognisync.com
- Issues: https://github.com/yourusername/cognisync/issues

## Acknowledgments

- Auditory-motor entrainment research community
- Parkinson's disease and stroke rehabilitation specialists
- Open-source contributors and libraries

## Roadmap

- [ ] Mobile application support
- [ ] Advanced AI prediction models
- [ ] Telehealth integration
- [ ] Multi-language support
- [ ] Wearable device integration
- [ ] Machine learning-based therapy optimization

---

**Note**: CogniSync is designed for clinical use under professional supervision. Always consult healthcare providers for medical advice.
