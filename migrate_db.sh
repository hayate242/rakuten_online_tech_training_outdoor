#!/bin/sh
rm -rf models/healthcare.db
python3 migrate_db.py
python3 seed_videos.py
python3 seed_categories.py
python3 seed_videoitems.py