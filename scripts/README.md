# Utility Scripts

This directory contains useful scripts to help with development and management.

## Available Scripts

### Initialize Database
Create all database tables:
```bash
python scripts/init_db.py
```

### Create Test User
Create an admin user for testing:
```bash
python scripts/create_user.py
```

Default credentials:
- Email: admin@example.com
- Username: admin
- Password: admin123

### Generate Secret Key
Generate a secure JWT secret key:
```bash
python scripts/generate_secret_key.py
```

## Notes

- Make sure all dependencies are installed before running these scripts
- For production environments, be sure to change the default password
- Backup your database before running scripts that modify data
