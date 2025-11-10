# Network Relativity Metrics

Compute these from your logs so we can publish them:

## Observation Velocity (v_o)

**Academic:** events_logged / wall_time during active data collection.

- Count of data collection events (e.g., participant sessions, measurements)
- Divide by total wall-clock time during active collection period
- Units: events per day or events per week

**Memetic:** valid_logs_per_day.

- Count of valid participant logs per day
- Filtered by inclusion/exclusion criteria
- Units: logs per day

## Verification Velocity (v_v)

**Academic:** verified_units_per_week through reviewer/editor path.

- Count of verified units (e.g., accepted manuscripts, peer-reviewed outcomes)
- Divide by time through review process
- Units: verified units per week

**Memetic:** curator-verified items per day.

- Count of curator-verified logs or batches per day
- Units: verified items per day

## Combined Metric (C_N)

C_N = (v_o * v_v) / (v_o + v_v) per arm

This represents the harmonic mean of observation and verification velocities.

## Trust-Modified Verification Velocity (v_v^(T))

**Academic trust proxy:**
- Acceptance rate of venue (0–1)
- Or inverse of number of review rounds (1 / rounds)
- T ∈ [0, 1]

**Memetic trust proxy:**
- Curator agreement % (0–1)
- Sensor corroboration % (0–1)
- T = (curator_agreement + sensor_corrob) / 2

v_v^(T) = v_v * T

## Reporting

Report for each arm:
- A-VTE (Academic Verification Time to Evidence)
- M-VTE (Memetic Verification Time to Evidence)
- ΔVTE (difference between arms)
- v_o, v_v, C_N, v_v^(T)

## Implementation

See `compute_vte.py` for VTE calculations.
See `compute_nr_metrics.py` (to be implemented) for Network Relativity metrics.

