-- Migration: 0001_create_form_submissions.sql
-- Table for storing all website form submissions in Cloudflare D1

CREATE TABLE IF NOT EXISTS form_submissions (
    id TEXT PRIMARY KEY,
    form_type TEXT NOT NULL,
    page_url TEXT,
    name TEXT,
    email TEXT,
    phone TEXT,
    submitted_data TEXT NOT NULL,
    submitted_at TEXT NOT NULL,
    email_status TEXT NOT NULL DEFAULT 'pending',
    email_message_id TEXT,
    email_error TEXT,
    ip_address TEXT,
    user_agent TEXT
);

CREATE INDEX IF NOT EXISTS idx_form_submissions_type ON form_submissions(form_type);
CREATE INDEX IF NOT EXISTS idx_form_submissions_date ON form_submissions(submitted_at);
CREATE INDEX IF NOT EXISTS idx_form_submissions_email ON form_submissions(email);
