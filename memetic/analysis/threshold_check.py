#!/usr/bin/env python3
"""
Check if memetic verification thresholds are met.

Reads memetic log data and computes:
- Effect direction consistency (≥ 70% with ΔEnergy ≥ +10)
- Replication count (≥ 150 participants across ≥ 3 cities)
- Sensor corroboration (≥ 60% with HRV or sleep improvements)
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


def load_logs(csv_path: str) -> List[Dict]:
    """Load memetic logs from CSV file."""
    logs = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(row)
    return logs


def check_effect_direction(logs: List[Dict]) -> tuple[float, int, int]:
    """
    Check if ≥ 70% show ΔEnergy ≥ +10.
    
    Returns: (percentage, count_positive, total_valid)
    """
    valid_logs = []
    for log in logs:
        try:
            energy_pre = int(log.get("energy_pre", 0))
            energy_post = int(log.get("energy_post", 0))
            delta = energy_post - energy_pre
            if delta >= 10:
                valid_logs.append(True)
            else:
                valid_logs.append(False)
        except (ValueError, TypeError):
            continue
    
    if not valid_logs:
        return 0.0, 0, 0
    
    count_positive = sum(valid_logs)
    total = len(valid_logs)
    pct = (count_positive / total) * 100
    
    return pct, count_positive, total


def check_replication(logs: List[Dict]) -> tuple[int, int]:
    """
    Check if ≥ 150 participants across ≥ 3 cities.
    
    Returns: (n_participants, n_cities)
    """
    cities = set()
    participants = set()
    
    for log in logs:
        pid = log.get("pid", "").strip()
        city = log.get("city", "").strip()
        
        if pid and city:
            participants.add(pid)
            cities.add(city)
    
    return len(participants), len(cities)


def check_sensor_corroboration(logs: List[Dict]) -> tuple[float, int, int]:
    """
    Check if ≥ 60% show HRV or sleep improvements.
    
    HRV: increase ≥ +5 ms
    Sleep: increase ≥ +2 percentage points
    
    Returns: (percentage, count_positive, total_quantified)
    """
    quantified_logs = []
    
    for log in logs:
        has_hrv = False
        has_sleep = False
        hrv_improved = False
        sleep_improved = False
        
        # Check HRV
        try:
            hrv_pre = float(log.get("hrv_rmssd_pre_24h", 0))
            hrv_post = float(log.get("hrv_rmssd_post_24h", 0))
            if hrv_pre > 0 and hrv_post > 0:
                has_hrv = True
                hrv_improved = (hrv_post - hrv_pre) >= 5.0
        except (ValueError, TypeError):
            pass
        
        # Check sleep
        try:
            sleep_pre = float(log.get("sleep_eff_pre", 0))
            sleep_post = float(log.get("sleep_eff_post", 0))
            if sleep_pre > 0 and sleep_post > 0:
                has_sleep = True
                sleep_improved = (sleep_post - sleep_pre) >= 2.0
        except (ValueError, TypeError):
            pass
        
        if has_hrv or has_sleep:
            quantified_logs.append(hrv_improved or sleep_improved)
    
    if not quantified_logs:
        return 0.0, 0, 0
    
    count_positive = sum(quantified_logs)
    total = len(quantified_logs)
    pct = (count_positive / total) * 100
    
    return pct, count_positive, total


def main():
    """Check all thresholds and report status."""
    data_path = Path("memetic/data/logs.csv")
    
    if not data_path.exists():
        print(f"Error: {data_path} not found")
        print("Create a CSV file with columns matching memetic_log.schema.json")
        return
    
    logs = load_logs(str(data_path))
    
    print("=" * 60)
    print("Memetic Verification Threshold Check")
    print("=" * 60)
    print()
    
    # Check 1: Effect Direction
    effect_pct, effect_pos, effect_total = check_effect_direction(logs)
    print(f"1. Effect Direction Consistency:")
    print(f"   {effect_pct:.1f}% show ΔEnergy ≥ +10 ({effect_pos}/{effect_total})")
    print(f"   Threshold: ≥ 70%")
    print(f"   Status: {'✓ PASS' if effect_pct >= 70 else '✗ FAIL'}")
    print()
    
    # Check 2: Replication
    n_participants, n_cities = check_replication(logs)
    print(f"2. Replication Count:")
    print(f"   {n_participants} participants across {n_cities} cities")
    print(f"   Threshold: ≥ 150 participants across ≥ 3 cities")
    print(f"   Status: {'✓ PASS' if n_participants >= 150 and n_cities >= 3 else '✗ FAIL'}")
    print()
    
    # Check 3: Sensor Corroboration
    sensor_pct, sensor_pos, sensor_total = check_sensor_corroboration(logs)
    print(f"3. Sensor Corroboration:")
    print(f"   {sensor_pct:.1f}% show HRV or sleep improvements ({sensor_pos}/{sensor_total} quantified)")
    print(f"   Threshold: ≥ 60% (target n ≥ 50 quantified)")
    print(f"   Status: {'✓ PASS' if sensor_pct >= 60 and sensor_total >= 50 else '✗ FAIL'}")
    print()
    
    # Overall status
    all_pass = (
        effect_pct >= 70 and
        n_participants >= 150 and
        n_cities >= 3 and
        sensor_pct >= 60 and
        sensor_total >= 50
    )
    
    print("=" * 60)
    print(f"Overall Status: {'✓ ALL CRITERIA MET' if all_pass else '✗ CRITERIA NOT MET'}")
    print("=" * 60)
    
    if all_pass:
        print("\nReady for curator audit (M5 milestone).")
    else:
        print("\nContinue data collection until all thresholds are met.")


if __name__ == "__main__":
    main()

