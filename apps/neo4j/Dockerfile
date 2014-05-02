# Neo4j Database Environment

# Start from an image with Java
FROM dockerfile/java

# Install dependencies
RUN apt-get -qq update  
RUN apt-get -qq install -y wget lsof

# Install Neo4j
WORKDIR /usr/bin  
RUN wget -q http://dist.neo4j.org/neo4j-community-2.0.1-unix.tar.gz  
RUN tar xf neo4j-community-2.0.1-unix.tar.gz  
RUN ln -s neo4j-community-2.0.1 neo4j

### NEW
#
# Configure to accept connections from outside the container
WORKDIR /usr/bin/neo4j/conf  
RUN cat neo4j-server.properties | sed "s/#org.neo4j.server.webserver.address/org.neo4j.server.webserver.address/g" > neo4j-server.properties.open  
RUN mv neo4j-server.properties.open neo4j-server.properties  
#
### NEW

# Expose the Neo4j default HTTP port 7474
EXPOSE 7474

# Entrypoint into running the Neo4j console
ENTRYPOINT /usr/bin/neo4j/bin/neo4j console  