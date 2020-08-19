class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None
def insertionSort(head_ref): 
	sorted1 = None
	current = head_ref 
	while (current != None): 
		nxt = current.next
		sorted1 = sortedInsert(sorted1, current) 
		current = nxt
	head_ref = sorted
	return head_ref 
def sortedInsert(head_ref, new_node): 
	current = None
	if (head_ref == None or (head_ref).data >= new_node.data): 
		new_node.next = head_ref 
		head_ref = new_node 
	else: 
		current = head_ref 
		while (current.next != None and
			current.next.data < new_node.data): 
			current = current.next
		new_node.next = current.next
		current.next = new_node 
	return head_ref 
def printList(head): 
	temp = head 
	while(temp != None): 
		print( temp.data, end = " ") 
		temp = temp.next
def push( head_ref, new_data): 
	new_node = Node(0) 
	new_node.data = new_data 
	new_node.next = (head_ref) 
	(head_ref) = new_node 
	return head_ref 
a = None
a = push(a, 5) 
a = push(a, 20) 
a = push(a, 4) 
a = push(a, 3) 
a = push(a, 30) 
print("Linked List before sorting ") 
printList(a) 
a = insertionSort(a) 
print("\nLinked List after sorting ") 
printList(a) 