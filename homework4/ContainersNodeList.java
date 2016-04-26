public class ContainersNodeList {

	private ContainersNode head;
	private int size;

	public ContainersNodeList() {
		this.head = null;
		this.size = 0;
	}

	public ContainersNodeList(ContainersNode head) {
		this.head = head;
		this.size = 1;
	}

	public void addToList(ContainersNode node) {
		if (this.size == 0) {
			this.head = node;
			this.size = 1;
		} else {
			node.setNext(head);
			this.head = node;
			this.size++;
		}
	}

	public ContainersNode getHead() {
		return this.head;
	}

	public int getSize() {
		return this.size;
	}
}
