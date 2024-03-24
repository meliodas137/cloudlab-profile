"""A bare bone profile to setup and deploy duckdb.

Instructions:
Wait for the profile instance to start, and then log in to the host via the
ssh port specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
 
# Create a raw PC
node = request.RawPC("node")

# Install and execute a script that is contained in the repository.
node.addService(rspec.Execute(shell="sh", command="/local/repository/setup.sh"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec(request)