public class ContainersNode {

	private int[] containers;
	private String previousAction;
	private ContainersNode father;
	private ContainersNode next;

	public ContainersNode(int[] containers, String previousAction) {
		this.containers = containers;
		this.previousAction = previousAction;
	}

	public void setFather(ContainersNode node) {
		this.father = node;
	}

	public void setNext(ContainersNode node) {
		this.next = node;
	}

	public int getContainer(int index) {
		return this.containers[index];
	}

	public String getPreviousAction() {
		return this.previousAction;
	}

	public ContainersNode getFather() {
		return this.father;
	}

	public ContainersNode getNext() {
		return this.next;
	}
}
