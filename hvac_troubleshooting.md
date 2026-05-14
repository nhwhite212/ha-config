
## Troubleshooting

### Units Not Responding to Automation
1. Check that the automation is enabled: **Settings → Automations → HVAC Season Control**
2. Check the automation trace: click the three dots next to the automation and select **Traces**
3. Verify the outside temperature sensor is working: check **Outside Temperature** on the dashboard
4. Make sure the Kumo integration is connected: **Settings → Devices & Services → Kumo**

### Presence Detection Wrong
1. Check **Someone Home** indicator on the dashboard
2. Go to **Developer Tools → States** and check `device_tracker.baysidea` 
   and `device_tracker.baysideb`
3. Make sure **Private WiFi Address** is turned off for the home network on both iPhones:
   **Settings → WiFi → tap network name → Private WiFi Address → Off**
4. Open the Home Assistant Companion app and force a location update
5. Check that the Home zone is correctly centered on your address:
   **Settings → Areas & Zones → Zones → Home**

### Units Running in Wrong Mode
1. Check the outside temperature vs your threshold settings on the dashboard
2. Run the automation manually: **Settings → Automations → HVAC Season Control → 
   three dots → Run**
3. Check the trace to see which condition was matched

### Kumo Integration Offline
1. Check **Settings → Devices & Services → Kumo** for any error messages
2. Verify your Mitsubishi units are powered on and connected to WiFi
3. Check that your Eero network is working
4. Try reloading the integration: three dots → **Reload**
5. If units show unavailable, restart Home Assistant: 
   **Settings → System → Restart**

### Outside Temperature Not Updating
1. Check the RTL_433 Raspberry Pi is powered on and connected to the network
2. Verify it is pointing to the correct Home Assistant IP (`192.168.4.21`)
3. Check **Developer Tools → States** for `sensor.outside_temperature_deck` 
   and look at the last updated time
4. As a backup, the OpenWeather integration provides outside temperature

### All Units Turned On When Nobody Home
1. Check the Away thresholds on the dashboard — if outside temp is above 
   Away Cool Threshold or below Away Heat Threshold the system will turn units on
2. Adjust the Away thresholds if needed
3. Check presence detection — if both phones show `not_home` but someone 
   is actually home, see Presence Detection section above

### Dashboard Not Loading
1. Try refreshing the browser
2. Clear browser cache
3. Access HA via `http://192.168.4.21:8123`
4. If HA IP has changed, check your Eero app for the current HA IP address —
   consider setting a static DHCP reservation for HA in the Eero app to 
   prevent this happening again

### After a Power Outage
1. Home Assistant should restart automatically
2. The Kumo integration may take a few minutes to reconnect to the units
3. If units don't reconnect, go to **Settings → Devices & Services → Kumo → Reload**
4. Check the RTL_433 Pi has also restarted and is sending temperature data

## Technical Notes
- Home Assistant is running at `http://192.168.4.21:8123`
- Home Assistant OS version: 17.3
- HA Core version: 2026.5.1
- hass-kumo version: 0.4.4
- The Kumo integration uses the Mitsubishi Comfort App V3 API for authentication
- Local control of units is via the Kumo WiFi adapters on your local network
- The RTL_433 receiver on a Raspberry Pi provides outdoor temperature dataEOF
