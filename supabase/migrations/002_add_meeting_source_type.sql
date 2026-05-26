-- Migration: 002_add_meeting_source_type
-- Adds 'meeting' to the source_type CHECK constraint on the documents table.
-- The original inline constraint is auto-named by Postgres as
-- documents_source_type_check; we drop it and replace with a named version.

alter table documents
  drop constraint if exists documents_source_type_check;

alter table documents
  add constraint documents_source_type_check
  check (
    source_type in (
      'code',
      'issue',
      'pr',
      'wiki',
      'discussion',
      'readme',
      'meeting'
    )
  );
