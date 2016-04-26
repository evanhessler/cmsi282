public class Containers {

	private ContainersNodeList root;

	public Containers(ContainersNode root) {
		this.root = new ContainersNodeList(root);
	}

	public String[] findSolution() {
		boolean foundSolution = false;
		ContainersNode currentNode = this.root.getHead();
		ContainersNode solutionNode = this.root.getHead();
		while (!foundSolution) {
			ContainersNodeList newList = new ContainersNodeList();
			while (currentNode != null && !foundSolution) {
				ContainersNode firstPossibility = this.empty(currentNode, 0);
				firstPossibility.setFather(currentNode);
				if (firstPossibility.getContainer(1) == 2 || firstPossibility.getContainer(2) == 2) {
					solutionNode = firstPossibility;
					foundSolution = true;
				}
				newList.addToList(firstPossibility);
				ContainersNode secondPossibility = this.empty(currentNode, 1);
				secondPossibility.setFather(currentNode);
				if (secondPossibility.getContainer(1) == 2 || secondPossibility.getContainer(2) == 2) {
					solutionNode = secondPossibility;
					foundSolution = true;
				}
				newList.addToList(secondPossibility);
				ContainersNode thirdPossibility = this.empty(currentNode, 2);
				thirdPossibility.setFather(currentNode);
				if (thirdPossibility.getContainer(1) == 2 || thirdPossibility.getContainer(2) == 2) {
					solutionNode = thirdPossibility;
					foundSolution = true;
				}
				newList.addToList(thirdPossibility);
				ContainersNode fourthPossibility = this.fill(currentNode, 0);
				fourthPossibility.setFather(currentNode);
				if (fourthPossibility.getContainer(1) == 2 || fourthPossibility.getContainer(2) == 2) {
					solutionNode = fourthPossibility;
					foundSolution = true;
				}
				newList.addToList(fourthPossibility);
				ContainersNode fifthPossibility = this.fill(currentNode, 1);
				fifthPossibility.setFather(currentNode);
				if (fifthPossibility.getContainer(1) == 2 || fifthPossibility.getContainer(2) == 2) {
					solutionNode = fifthPossibility;
					foundSolution = true;
				}
				newList.addToList(fifthPossibility);
				ContainersNode sixthPossibility = this.fill(currentNode, 2);
				sixthPossibility.setFather(currentNode);
				if (sixthPossibility.getContainer(1) == 2 || sixthPossibility.getContainer(2) == 2) {
					solutionNode = sixthPossibility;
					foundSolution = true;
				}
				newList.addToList(sixthPossibility);
				ContainersNode seventhPossibility = this.transfer(currentNode, 0, 1);
				seventhPossibility.setFather(currentNode);
				if (seventhPossibility.getContainer(1) == 2 || seventhPossibility.getContainer(2) == 2) {
					solutionNode = seventhPossibility;
					foundSolution = true;
				}
				newList.addToList(seventhPossibility);
				ContainersNode eighthPossibility = this.transfer(currentNode, 1, 0);
				eighthPossibility.setFather(currentNode);
				if (eighthPossibility.getContainer(1) == 2 || eighthPossibility.getContainer(2) == 2) {
					solutionNode = eighthPossibility;
					foundSolution = true;
				}
				newList.addToList(eighthPossibility);
				ContainersNode ninthPossibility = this.transfer(currentNode, 0, 2);
				ninthPossibility.setFather(currentNode);
				if (ninthPossibility.getContainer(1) == 2 || ninthPossibility.getContainer(2) == 2) {
					solutionNode = ninthPossibility;
					foundSolution = true;
				}
				newList.addToList(ninthPossibility);
				ContainersNode tenthPossibility = this.transfer(currentNode, 2, 0);
				tenthPossibility.setFather(currentNode);
				if (tenthPossibility.getContainer(1) == 2 || tenthPossibility.getContainer(2) == 2) {
					solutionNode = tenthPossibility;
					foundSolution = true;
				}
				newList.addToList(tenthPossibility);
				ContainersNode eleventhPossibility = this.transfer(currentNode, 1, 2);
				eleventhPossibility.setFather(currentNode);
				if (eleventhPossibility.getContainer(1) == 2 || eleventhPossibility.getContainer(2) == 2) {
					solutionNode = eleventhPossibility;
					foundSolution = true;
				}
				newList.addToList(eleventhPossibility);
				ContainersNode twelvethPossibility = this.transfer(currentNode, 2, 1);
				twelvethPossibility.setFather(currentNode);
				if (twelvethPossibility.getContainer(1) == 2 || twelvethPossibility.getContainer(2) == 2) {
					solutionNode = twelvethPossibility;
					foundSolution = true;
				}
				newList.addToList(twelvethPossibility);
				currentNode = currentNode.getNext();
			}
			currentNode = newList.getHead();
		}
		ContainersNode tempNode = solutionNode;
		int numOfSteps = 0;
		while (tempNode != null) {
			numOfSteps++;
			tempNode = tempNode.getFather();
		}
		tempNode = solutionNode;
		String[] result = new String[6];
		for (int i = 5; i >= 0; i--) {
			result[i] = tempNode.getPreviousAction();
			tempNode = tempNode.getFather();
		}
		return result;
	}

	public ContainersNode empty(ContainersNode node, int index) {
		int[] containers = new int[3];
		String previousAction = "";
		if (index == 0) {
			containers[0] = 0;
			containers[1] = node.getContainer(1);
			containers[2] = node.getContainer(2);
			previousAction = "E10";
		} else if (index == 1) {
			containers[0] = node.getContainer(0);
			containers[1] = 0;
			containers[2] = node.getContainer(2);
			previousAction = "E7";
		} else {
			containers[0] = node.getContainer(0);
			containers[1] = node.getContainer(1);
			containers[2] = 0;
			previousAction = "E4";
		}
		ContainersNode resultNode = new ContainersNode(containers, previousAction);
		return resultNode;
	}

	public ContainersNode fill(ContainersNode node, int index) {
		int[] containers = new int[3];
		String previousAction = "";
		if (index == 0) {
			containers[0] = 10;
			containers[1] = node.getContainer(1);
			containers[2] = node.getContainer(2);
			previousAction = "F10";
		} else if (index == 1) {
			containers[0] = node.getContainer(0);
			containers[1] = 7;
			containers[2] = node.getContainer(2);
			previousAction = "F7";
		} else {
			containers[0] = node.getContainer(0);
			containers[1] = node.getContainer(1);
			containers[2] = 4;
			previousAction = "F4";
		}
		ContainersNode resultNode = new ContainersNode(containers, previousAction);
		return resultNode;
	}

	public ContainersNode transfer(ContainersNode node, int indexA, int indexB) {
		int[] containers = new int[3];
		containers[0] = node.getContainer(0);
		containers[1] = node.getContainer(1);
		containers[2] = node.getContainer(2);
		String previousAction = "T";
		if (indexA == 0) {
			previousAction += "10";
			if (indexB == 1) {
				previousAction += "7";
			} else {
				previousAction += "4";
			}
		} else if (indexA == 1) {
			previousAction += "7";
			if (indexB == 0) {
				previousAction += "10";
			} else {
				previousAction += "4";
			}
		} else {
			previousAction += "4";
			if (indexB == 0) {
				previousAction += "10";
			} else {
				previousAction += "7";
			}
		}
		if (indexB == 0) {
			if (node.getContainer(indexA) + node.getContainer(indexB) > 10) {
				containers[0] = 10;
				containers[indexA] = (node.getContainer(indexA) - (10 - node.getContainer(indexB)));
			} else {
				containers[0] = node.getContainer(indexA) + node.getContainer(indexB);
				containers[indexA] = 0;
			}
		} else if (indexB == 1) {
			if (node.getContainer(indexA) + node.getContainer(indexB) > 7) {
				containers[1] = 7;
				containers[indexA] = (node.getContainer(indexA) - (7 - node.getContainer(indexB)));
			} else {
				containers[1] = node.getContainer(indexA) + node.getContainer(indexB);
				containers[indexA] = 0;
			}
		} else {
			if (node.getContainer(indexA) + node.getContainer(indexB) > 4) {
				containers[2] = 4;
				containers[indexA] = (node.getContainer(indexA) - (4 - node.getContainer(indexB)));
			} else {
				containers[2] = node.getContainer(indexA) + node.getContainer(indexB);
				containers[indexA] = 0;
			}
		}
		ContainersNode resultNode = new ContainersNode(containers, previousAction);
		return resultNode;
	}

	public static void main(String[] args) {
		int[] testContainers = {0, 7, 4};
		String previousAction = "Beginning Node Initialized at [0, 7, 4]";
		ContainersNode node = new ContainersNode(testContainers, previousAction);
		Containers test = new Containers(node);
		String[] result = test.findSolution();
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}
	}
}
