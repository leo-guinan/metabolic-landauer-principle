#!/usr/bin/env python3
"""
Compute Verification Time to Evidence (VTE) for both academic and memetic arms.

Reads milestone JSONL files and computes:
- A-VTE: Time from hypothesis lock to external acceptance + evidence threshold
- M-VTE: Time from hypothesis lock to all four verification criteria met
- ΔVTE: Difference between arms
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Optional


def parse_timestamp(ts: str) -> datetime:
    """Parse ISO-8601 timestamp, handling Z suffix."""
    if ts.endswith("Z"):
        ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)


def load_milestones(arm: str) -> List[Dict]:
    """Load milestones from JSONL file."""
    path = Path(f"{arm}/milestones/milestones.jsonl")
    if not path.exists():
        return []
    
    milestones = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                milestones.append(json.loads(line))
    return milestones


def vte_academic(milestones: List[Dict]) -> Optional[float]:
    """Compute A-VTE: time from A0 to A6 (external acceptance)."""
    # Find start (A0)
    start_milestones = [m for m in milestones if m.get("code") == "A0"]
    if not start_milestones:
        return None
    start = parse_timestamp(start_milestones[0]["ts"])
    
    # Find stop (A6 - external acceptance)
    # Note: Evidence threshold (A-EvidenceThreshold) should be verified separately
    # in analysis artifacts. This computes time to acceptance.
    stop_milestones = [m for m in milestones if m.get("code") == "A6"]
    if not stop_milestones:
        return None
    stop = parse_timestamp(stop_milestones[0]["ts"])
    
    return (stop - start).total_seconds()


def vte_memetic(milestones: List[Dict]) -> Optional[float]:
    """Compute M-VTE: time from M0 to M4+M5 (all criteria met)."""
    # Find start (M0)
    start_milestones = [m for m in milestones if m.get("code") == "M0"]
    if not start_milestones:
        return None
    start = parse_timestamp(start_milestones[0]["ts"])
    
    # Find stop (M4 or M5 - whichever comes first when all criteria are met)
    stop_milestones = [m for m in milestones if m.get("code") in ["M4", "M5"]]
    if not stop_milestones:
        return None
    
    # Use earliest timestamp
    stop_times = [parse_timestamp(m["ts"]) for m in stop_milestones]
    stop = min(stop_times)
    
    return (stop - start).total_seconds()


def format_duration(seconds: float) -> str:
    """Format duration in human-readable form."""
    days = seconds / 86400
    hours = (seconds % 86400) / 3600
    minutes = (seconds % 3600) / 60
    
    parts = []
    if days >= 1:
        parts.append(f"{int(days)} days")
    if hours >= 1:
        parts.append(f"{int(hours)} hours")
    if minutes >= 1:
        parts.append(f"{int(minutes)} minutes")
    
    return ", ".join(parts) if parts else f"{int(seconds)} seconds"


def main():
    """Main computation and reporting."""
    academic_milestones = load_milestones("academic")
    memetic_milestones = load_milestones("memetic")
    
    a_vte = vte_academic(academic_milestones)
    m_vte = vte_memetic(memetic_milestones)
    
    print("=" * 60)
    print("Verification Time to Evidence (VTE) Report")
    print("=" * 60)
    print()
    
    if a_vte is not None:
        print(f"Academic VTE (A-VTE): {format_duration(a_vte)}")
        print(f"  ({a_vte:.0f} seconds)")
    else:
        print("Academic VTE: Not yet computed (missing milestones)")
    
    print()
    
    if m_vte is not None:
        print(f"Memetic VTE (M-VTE): {format_duration(m_vte)}")
        print(f"  ({m_vte:.0f} seconds)")
    else:
        print("Memetic VTE: Not yet computed (missing milestones)")
    
    print()
    
    if a_vte is not None and m_vte is not None:
        delta = a_vte - m_vte
        print(f"ΔVTE (A-VTE - M-VTE): {format_duration(abs(delta))}")
        if delta > 0:
            print(f"  (Academic arm is {format_duration(delta)} slower)")
        elif delta < 0:
            print(f"  (Memetic arm is {format_duration(abs(delta))} slower)")
        else:
            print("  (Both arms completed simultaneously)")
    else:
        print("ΔVTE: Cannot compute (one or both arms incomplete)")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()

