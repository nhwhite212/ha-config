paste the entire markdown content here
cat > /config/hvac_documentation.md << 'EOF'
paste the entire markdown content here
# HVAC Automation System Documentation

## Overview
This system automatically controls the Mitsubishi Kumo (Comfort App) HVAC units based on 
outside temperature and presence detection. It replaces the Comfort App's winter/summer 
seasonal setting with a more intelligent, automated approach.

## How It Works

### Presence Detection
The system determines if someone is home based on the location of two cell phones 
(Baysidea and Baysideb). If either phone is detected at home, the system considers 
the house occupied.

### Operating Modes

#### Someone Home
- **Shoulder Season** (between Heat and Cool thresholds): Units are left alone. 
  Anyone can control their zone manually from the dashboard, the Comfort app, or 
  the local zone controller.
- **Hot Weather** (above Cool Threshold): Any units that are already running are 
  switched to **Cool** mode. Units that are off are left off.
- **Cold Weather** (below Heat Threshold): Any units that are already running are 
  switched to **Heat** mode. Units that are off are left off.

#### Nobody Home
- **Shoulder Season** (between Away thresholds): All units are turned **off**.
- **Very Hot** (above Away Cool Threshold): All units turn on in **Cool** mode 
  and are set to the Away Cool Setpoint temperature to protect the house.
- **Very Cold** (below Away Heat Threshold): All units turn on in **Heat** mode 
  and are set to the Away Heat Setpoint temperature to protect pipes and the house.

## Dashboard Controls

### HVAC Settings Card
All thresholds and setpoints can be adjusted from the dashboard using sliders:

| Setting | Description | Default |
|---------|-------------|---------|
| Cool Threshold | Outside temp above which running units switch to Cool (occupied) | 75°F |
| Heat Threshold | Outside temp below which running units switch to Heat (occupied) | 55°F |
| Away Heat Threshold | Outside temp below which heat turns on when nobody home | 45°F |
| Away Cool Threshold | Outside temp above which AC turns on when nobody home | 85°F |
| Away Heat Setpoint | Temperature to heat to when nobody home | 62°F |
| Away Cool Setpoint | Temperature to cool to when nobody home | 85°F |

### Status Indicators
- **Someone Home**: Shows whether the system thinks anyone is home
- **Outside Temperature**: Current reading from the deck weather station

### Thermostat Cards
Each zone has its own thermostat card showing:
- Current room temperature
- Target temperature setpoint
- Current mode (heat/cool/off/auto)

You can manually adjust any zone from these cards at any time.

### Buttons
- **All Units Off**: Immediately turns off all 5 zones

## Manual Control
You can always override the automation by:
- Adjusting any unit from its thermostat card on the dashboard
- Using the Comfort app on your phone
- Using the local zone controller on the wall unit
- Asking Alexa to change a specific unit

## Zones
The system controls 5 zones:
- Living Room
- Dining Room
- Bedroom
- Master Bedroom
- Home Office

## Automation Schedule
The automation runs:
- Every 30 minutes
- Whenever either phone changes location (arriving or leaving home)
- Whenever the outside temperature changes

## Tips
- In shoulder season (between 55°F and 75°F), just use the local controls — 
  the automation won't interfere
- If you want to temporarily disable the automation, go to 
  **Settings → Automations → HVAC Season Control** and toggle it off
- The away thresholds are intentionally more extreme than the occupied thresholds — 
  they're meant to protect the house, not keep it comfortable
