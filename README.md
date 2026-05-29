# SkillBridge Training Management System for Odoo 19

A complete Training Institute ERP built on Odoo 19 – manage students, instructors, bootcamps, batches, sessions, assignments, attendance, and dashboard analytics.

## Features

- **Student Management** – registration, portal access, batch assignment
- **Instructor Management** – profiles, session scheduling
- **Bootcamp / Course Management** – categorization, duration, status
- **Batch & Class Scheduling** – capacity, start/end dates, instructor assignment
- **Session Planning** – calendar view, drag‑drop scheduling, room allocation
- **Assignment Tracking** – submission, grading, due dates
- **Attendance Management** – daily per‑session attendance
- **Dashboard** – real‑time KPIs (students, instructors, bootcamps, ongoing sessions)
- **Automated Reminders** – email notifications for upcoming sessions (cron job)
- **Multi‑company Ready** – branch isolation via security groups

## Installation

1. Copy the `training_ms` folder into your Odoo `custom-addons` directory.
2. Install dependencies: `hr`, `calendar` (if not already installed).
3. Restart Odoo and upgrade the apps list.
4. Install the module from Apps → SkillBridge Training Management.

## Dependencies

- Odoo 19 (Community or Enterprise)
- Python 3.11+
- PostgreSQL 16+
- Modules: `base`, `mail`, `contacts`, `hr`, `calendar`, `web`

## Configuration

- **User Groups**: `SkillBridge User` (basic access) and `SkillBridge Manager` (full control).
- **Email Reminders**: Configure outgoing mail server in Odoo. The cron runs every hour.
- **Multi‑company**: Assign users to companies; the module supports branch isolation.

## Usage

- After installation, find the **SkillBridge** top‑menu with all sub‑menus.
- Create a bootcamp → batch → sessions.
- Enroll students into batches, track attendance and assignments.
- The dashboard shows key metrics automatically.

## Screenshots

(Add screenshots here if you have them)

## License

LGPL-3

## Author

Galana G. – built for Odoo 19

## Support

For issues or customizations, please open an issue on GitHub.
