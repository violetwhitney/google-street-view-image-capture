import subprocess


# Open the file and remember the lines of the file.
locations_csv = []
with open('family-dollar-data.csv', 'r') as f:
    locations_csv = f.readlines()

# Parse the file by taking each line, grabbing the lat and lon values as floats,
# and storing in the "locations" array.
locations = []
for line in locations_csv[1:]:
    cells = line.split(",")
    lat = float(cells[0])
    lon = float(cells[1])
    location = (lat, lon)
    locations.append(location)

# Prepare the url for interpolation.
base_url = "https://maps.googleapis.com/maps/api/streetview?size=640x400&location={0},{1}&fov=90&heading={2}&pitch=10&key=AIzaSyAMw209rAV8zEjzD1_Fz5FPpx9WIJ7C1G8"

row = 2
headings = [0, 90, 180, 270]

# Loop over every location, and for each location, loop over all the possible headings.
for location in locations:
    for heading in headings:
        # Create the URL for the request to Google.
        lat = location[0]
        lon = location[1]
        url = base_url.format(lat, lon, heading)

        # Create the filename we want to save as, e.g. family-dollar-2-90.jpg.
        filename = "familydollar-{0}-{1}.jpg".format(row, heading)

        # Use the 'curl' command to actually make the request and save the file to disk.
        subprocess.call(["curl", url, "-o", filename])

    # Increment the row to correlate with the Excel file.
    row += 1

