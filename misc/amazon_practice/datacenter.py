# Given a data center with n servers from 1 to n. To make the data center running, all servers must be connected, that means there exists at least one path between any pair of servers. Now we know there could be some critical connections broken which brings down the whole data center. You need to write a program to find out all these broken critical connections. A server connection is a critical connection which when removed will make the whole data center disconnected.
# Write a method to output all critical connections.

# Input:
# serversNum, the number of servers in the data center.
# connectionsNum, the number of connections between the servers.
# connections, a list of pairs representing the connections between two severs.

# Output:
# Return a list of integer pairs representing the critical connections. Output an empty array if there are no critical connections.
# Example :
# Input:
# serversNum = 4
# connectionsNum = 4
# connections = [[1, 2], [1, 3], [3, 2], [3, 4]]

# Output:
# [[3,4]]
# Explanation:
# There are one critical connections:
# 1. Between server 3 and 4
# If the connection [3, 4] breaks, then the network will be disconnected since servers 3 and 4 cannot communicate with the rest of the network.
# Remaining three connections are not critical.
#------------------#

# minimum spanning tree (traveling salesman/connections)
# turn connections list into a dict of connections(graph) for each value
#connections = [[1, 2], [1, 3], [3, 2], [3, 4]]
#serversNum = 4
#connectionsNum = 4
connections = [[1, 2], [2, 3], [4, 3], [4, 5], [5, 7], [6, 7], [7, 8]] 
serversNum = 8
connectionsNum = 7


def createDict(connections):
    dic = {}
    for a, b in connections:
        dic.setdefault(a, []).append(b)
        dic.setdefault(b, []).append(a)
    return dic

def findCriticalConn(serversNum, connectionsNum, connections):
    output = []
    dic = createDict(connections)
    #find servers with just one connection
    #start from one, pop connections
    for s in dic:
        if len(dic[s]) == 1:
            output.append()
            #build a new dict with first connection removed
            
    return output

print(findCriticalConn(serversNum, connectionsNum, connections))
