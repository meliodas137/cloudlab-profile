"""A bare bone profile to setup and deploy duckdb.

Instructions:
Wait for the profile instance to start, and then log in to the host via the
ssh port specified below.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.RawPC("node")

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="echo \"...Initializing node...\""))
node.addService(pg.Execute(shell="sh", command="chmod +x /local/repository/setup.sh"))
node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)