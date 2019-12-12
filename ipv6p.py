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
		("How many bytes does an IPv6 address have?", "16", "IPv4 has 4 bits per block: 0-255 (four times in X.Y.Z.W). Therefore: 8b.8b.8b.8b = 8 bits * 4 = 32 bits = 4 bytes. Try the same for IPv6."),
		("How many bits does an IPv6 address have?", "128", "IPv4 has 4 bits per block: 0-255 (four times in X.Y.Z.W). Therefore: 8b.8b.8b.8b = 8 bits * 4 = 32 bits. Try the same for IPv6."),
		("How much larger is an IPv6 address compared to an IPv4 address?", "2^96", "Two to the power of what? (Answer type: 2^?). IPv4 = 2^32, IPv6 = 2^?, therefore ..."),
		("What notation is used to replace one or more blocks with all zeroes?", "::", "E.g.: 2001:610:158:bad0:0000:0000:0000:1234 has three blocks."),
		("How often can you replace a block with a shortening notation (number only)?", "1", "Would 2001::158::bad0 make sense?"),
		("Does IPv6 have broadcast addresses (yes/no)?", "no", "These are replaced by multicast."),
		("Does IPv6 have subnet masks (yes/no)?", "no", ""),
		("Does IPv6 have prefixes (yes/no)?", "yes", ""),
		("What is the use of the ::/7 address range?", "special purpose", ""),
		("What does the ::/7 address range consist of (answer format: ::X and Y::/Z)?", "::/8 and 100::/8", ""),
		("What is the use of the 2000::/3 address range?", "global unicast", ""),
		("What is the use of the fc00::/7 address range?", "unique local unicast", ""),
		("What is the use of the fe80::/10 address range?", "link local unicast", ""),
		("What is the use of the ff00::/8 address range?", "multicast", ""),
		("What is the the address range of the global unicast?", "2000::/3", ""),
		("What is the the address range of the unique local unicast?", "fc00::/7", ""),
		("What is the the address range of the link-local unicast?", "fe80::/10", ""),
		("What is the the address range of multicast?", "ff00::/8", ""),
		("What is the use of the address range of ::/128?", "unspecified address", "Think of the /128 and how many bits an IPv6 address has."),
		("What is the use of the following IPv6 address: ::1/128?", "localhost", "Equivalent of 127.0.0.1."),
		("How does one make the IPv4 address compatible in an IPv6 address (include the range): x.y.z.w?", "::x.y.z.w/128", "Don't forget the : vs .!"),
		("How does one create an IPv4 mapped address (include the range)?", "::ffff:0:0/96", ""),
		("What is the non-local well-known prefix of IPv6 (include the range)?", "64:ff9b::/96", ""),
		("What is the well-known prefix for local use (include the range)?", "64:ff9b:1::/48", ""),
		("What was the main usage of IPv4 compatible addresses (now deprecated)?", "automatic tunneling", ""),
		("What is the use of the address range of 100::/64?", "discard only address block", "'The black hole'"),
		("What is the discard only address block of IPv6?", "100::/64", "'The black hole'"),
		("What is the first RIR address space?", "2001::/16", "RIR = Regional Internet Registries, such as RIPE NCC, ARIN, APNIC, LACNIC, AfriNIC."),
		("What is the 6to4 address space?", "2002::/16", ""),
		("How many large chunks of IPv6 address ranges were allocated on October 3rd, 2006 (number only)?", "5", ""),
		("Name the allocated IPv6 large chunks that were allocated on October 3rd, 2006 (in chronological order, separated by space)?", "2400::/12 2600::/12 2800::/12 2a00::/12 2c00::/12", ""),
		("What is the grow potential of the large chunk 2400::/12?", "2400::/7", ""),
		("What is the address range of TEREDO?", "2001::/32", "It's in the 2001::/23 range"),
		("What is the address range for benchmarking purposes?", "2001:2::/48", "It's in the 2001::/23 range"),
		("What is the address range of AS112-v6?", "2001:4:112::/48", "It's in the 2001::/23 range"),
		("What is the address range of ORCHIDv2?", "2001:20::/28", "It's in the 2001::/23 range"),
		("Statement: The anycast address is allocated from the (global) unicast address space (true/false).", "true", ""),
		("Statement: The anycast address is allocated from the (global) multicast address space (true/false).", "false", ""),
		("The anycast address is allocated from the (global) _______ address space.", "unicast", ""),
		("Statement: Address reuse is possible on the other link in the fe80::/10 address space (true/false).", "true", "What is the fe80::/10 address space used for?"),
		("Statement: ff00::/8 can be written as ff::/8 (true/false).", "false", ""),
		("How can this IPv6 address be shortened: fe80:0000:0353:0000:0f21:0001:0003:ffff?", "fe80::353:0000:f21:1:3:ffff", "Remember that '::' can only be done once!"),
		("What is the pre-defined multicast address for all link-local nodes?", "ff02::1", ""),
		("What is the pre-defined multicast address for all link-local routers?", "ff02::2", ""),
		("What is the pre-defined multicast address for all site-local routers?", "ff05::2", ""),
		("Statement: ping6 ff02::1 will always get you a result (true/false).", "false", ""),
		("Statement: IPv6 addresses consist of decimal-only characters (true/false).", "false", ""),
		("Statement: The ':' in an IPv6 addresses can always be replaced by '.' (true/false).", "false", ""),
		("What does RIR stand for?", "regional internet registries", ""),
		("Statement: IPv6 uses ARP (true/false).", "true", ""),
		("Statement: IPv6 replaced ARP for the Neighbor Discovery Protocol (true/false).", "true", ""),
		("What does NDP stand for?", "neighbor discovery protocol", "Was used instead of ARP."),
		("Statement: IPv6 uses ICMPv6 to discover or apply (true/false).", "true", ""),
		("Statement: ICMPv6 can be used to detect duplicate addresses (true/false).", "true", ""),
		("Statement: Address and status of neighbors can be found using ICMPv6 (true/false).", "true", ""),
		("What is the ICMPv6 type of the Router Solicitation for NDP (number only)?", "133", "It's in the range of 133-137"),
		("What is the ICMPv6 type of the Router Advertisement for NDP (number only)?", "134", "It's in the range of 133-137"),
		("What is the ICMPv6 type of the Neighbor Solicitation for NDP (number only)?", "135", "It's in the range of 133-137"),
		("What is the ICMPv6 type of the Neighbor Advertisement for NDP (number only)?", "136", "It's in the range of 133-137"),
		("What is the ICMPv6 type of the Redirect Message for NDP (number only)?", "137", "It's in the range of 133-137"),
		("What does the ICMPv6 type of 133 mean in NDP?", "router solicitation", ""),
		("What does the ICMPv6 type of 134 mean in NDP?", "router advertisement", ""),
		("What does the ICMPv6 type of 135 mean in NDP?", "neighbor solicitation", ""),
		("What does the ICMPv6 type of 136 mean in NDP?", "neighbor advertisement", ""),
		("What does the ICMPv6 type of 137 mean in NDP?", "redirect message", ""),
		("What does SLAAC stand for?", "stateless address autoconfiguration", ""),
		("What is the requirement for SLAAC before it can send out a Router Advertisement?", "link local address", "It's an address."),
		("What is the next step for SLAAC after it has a link local address?", "router advertisement", ""),
		("What does DAD stand for?", "duplicate address detection", "dup... addr.. det...")
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
