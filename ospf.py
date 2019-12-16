#########################
# IPv6 Practice         #
# Made by Ivar Slotboom #
#########################

### Import
import random

### Globals

### Funcs
def AskCharacteristics():
	questions = [
		# (Question, Answer, Hint)
		("What is an LSP?", "link state packet", "p is usually 'protocol' or 'packet'."),
		("What kind of algorithm is Dijkstra?", "single source shortest path", ""),
		("Link State Packets represent the state of a ______ and its links to the rest of the network", "router", "A network device"),
		("What does NBMA stand for?", "non broadcast multiple access", ""),
		("Broadcast networks (LANs) and NBMA networks are represented by ______ ______ inside the topology", "virtual nodes", ""),
		("What does DR stand for?", "designated router", ""),
		("How do hosts find their neighbors in a point to point link?", "hello packets", "Starts with a greeting!"),
		("After sending a hello packet on a point to point link, both ends will become ______", "adjacent", ""),
		("With broadcast (and NBMA) networks, you want to use ______ if possible on broadcast networks to send hello packets.", "multicast", ""),
		("Statement: (Broadcast/NBMA) Every neighbor will eventually become adjacent (true/false).", "false", "Only those that are neighbors in the virtual topology"),
		("Statement: (Broadcast/NBMA) One of the adjacent routers is always a (B)DR (true/false).", "true", "Of course you need this!"),
		("On broadcast (and NBMA) networks, one of the adjacent neighbor will always be a ______.", "(b)dr", ""),
		("The LSRefreshTime is __ ______.", "30 minutes", ""),
		("The RIP refresh time for its tables is __ _______.", "30 seconds", ""),
		("Statement: Detection of new neighbors will come up in the 30 minute update packet (true/false).", "false", "This is sent ASAP."),
		("Statement: Detection of a link or node failure will be sent as soon as possible (true/false).", "true", ""),
		("Statement: Change of link cost will be sent out as soon as possible (true/false).", "true", ""),
		("Statement: LSPs never arrive out of order over the network (true/false).", "false", ""),
		("Statement: LSPs use timestamps to mitigate packets that are out of order (true/false).", "false", "Timestamps cause trouble if clocks are not synchronized or out of order!"),
		("Statement: LSPs use sequence numbers to mitigate packets that are out of order (true/false).", "true", ""),
		("OSPF introduces ______ routing", "hierarchical", ""),
		("How many levels does OSPF use (number only)?", "2", ""),
		("Statement: OSPF does not support subnets (true/false).", "false", ""),
		("OSPF uses efficient ______ for flooding", "multicast", ""),
		("In contrast to point-to-point, there is also point-to-_______", "multipoint", ""),
		("Statement: OSPF supports virtual links for backbone connectivity (true/false).", "true", ""),
		("Statement: OSPF supports load balancing (true/false).", "true", ""),
		("Statement: OSPF supports unnumbered of interfaces/networks (true/false).", "true", "UNLIMITED POWERRRRRR"),
		("Statement: OSPF does not support authentication yet (true/false).", "false", ""),
		("Statement: IS-IS = 0 (true/false).", "true", "OSPF fun :)"),
		("Statement: OSPF works directly on top of UDP (true/false).", "false", "It's actually IP!"),
		("Statement: OSPF works directly over IP (true/false).", "true", ""),
		("OSPF uses protocol type __ (number only)", "89", "Why was 6 afraid of 7? Because 7 ___ ___."),
		("LSA stands for ___ ____ ___", "link state advertisement", ""),
		("In OSPF, what is the default timer for a HelloInterval?", "10 seconds", ""),
		("In OSPF, what is the default timer for a RouterDeadInterval?", "40 seconds", ""),
		("In the case of a database overflow, ______ routing information is dropped first.", "external", ""),
		("Statement: LSAs need not to be acknowledged by others (true/false).", "false", "They do!"),
		("How are DRs and BDRs elected?", "hello packets", "It's a packet"),
		("The (B)DR represents the network as a ______ ______ in the graph and acts on the network's behalf.", "virtual node", ""),
		("Statement: The priority of routers can not be configured in OSPF (true/false).", "false", ""),
		("What is the IPv4 multicast address to AllDRouters?", "224.0.0.6", "IPv4 address"),
		("What is the IPv4 multicast address to AllSPFRouters?", "224.0.0.5", "IPv4 address"),
		("What is the IPv6 multicast address to AllDRouters?", "ff02::6", "IPv6 address"),
		("What is the IPv6 multicast address to AllSPFRouters?", "ff02::5", "IPv6 address"),
		("Statement: Area 1 is the backbone area (true/false).", "false", "We start counting at 0 :-)"),
		("Statement: Non-backbone areas are called 'limbs' (true/false).", "true", ""),
		("Non-backbone areas are often called _____.", "limbs", ""),
		("ABR stands for ___________.", "area border router", ""),
		("ASBR stands for ___________.", "autonomous system boundary router", ""),
		("IAS stands for _______.", "inter area summaries", ""),
		("A stub(by) area is an area into which __ ______ routing information is injected bu the ABRs.", "no external", ""),
		("A stub(by) area uses a _____ _____ for all external destinations", "default route", ""),
		("A totally stubby area is a stubby area into which not even ____ ____ summaries are injected.", "inter area", ""),
		("What does the OSPF packer header look like (names only, separated by space)?", "version type packet length router id area id checksum autype authentication", ""),
		("How many types are there for the OSPF packet header (number only)?", "5", ""),
		("How many autypes are there for the OSPF packet header (number only)?", "3", ""),
		("What are the OSPF packet types (names only, separated by space)?", "hello database description link state request link state update link state acknowledgement", ""),
		("Statement: The OSPF hello packet includes the MAC address of the DR and BDR (true/false)", "false", ""),
		("Statement: The OSPF hello packet includes the IP address of the DR and BDR (true/false)", "true", ""),
		("What does NSSA stand for?", "not so stubby area", ""),
		("What is the Link State ID of 'Router ID of originating router'?", "1", ""),
		("What is the Link State ID of 'IP address of the network's DR'?", "2", ""),
		("What is the Link State ID of 'The destination network's prefix'?", "3", ""),
		("What is the Link State ID of 'Router ID of described ASBR'?", "4", ""),
		("What is the Link State ID of 'The destination network's prefix'?", "5", ""),
		("What is the Link State ID of 'Router ID of originating router'?", "7", ""),
		("What does it mean if the 'I' bit is set in an OSPF DD packet header?", "init bit (first packet)", ""),
		("What does it mean if the 'M' bit is set in an OSPF DD packet header?", "more bit (more packets follow)", ""),
		("What does it mean if the 'MS' bit is set in an OSPF DD packet header?", "master/slave bit", "")
		# Don't forget to remove the , at the end!
	]

	random.shuffle(questions)

	# Ask questions
	q = 0
	for question in questions:
		q += 1
		printHint = False
		while True:
			print("Question {}/{}:".format(q, len(questions)))
			print("(Type answer to show the answer or skip to skip this question.)")
			print("{}\n".format(question[0]))

			if printHint and question[2] != "":
				print("\tHint: {}\n".format(question[2]))

			answer = input("> ")
			answer = answer.replace("-", " ")
			answer = answer.lower()
			if answer == question[1]:
				print("Correct!\n")
				break
			elif answer == "skip":
				break
			elif answer == "answer":
				print("The answer is: {}".format(question[1]))
			elif "/" in question[1]:
				if answer == question[1].split("/")[0]:
					print("Don't forget the subnet!")
				else:
					print("Incorrect.")
				printHint = True
			else:
				print("Incorrect.")
				printHint = True
			print("")

# https://www.os3.nl/_media/2019-2020/courses/inr/ipv6.pdf

### Main
def main():
	AskCharacteristics()

if __name__ == "__main__":
    # execute only if run as a script
    main()
