class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 트리 삽입 함수
def insert(root, data):
    if root is None:
        node = TreeNode()
        node.data = data
        return node

    if data < root.data:
        root.left = insert(root.left, data)  # 왼쪽 서브트리로 삽입
    else:
        root.right = insert(root.right, data)  # 오른쪽 서브트리로 삽입
    return root

# 트리 탐색 함수
def search(root, find_group):
    current = root
    while current:
        if find_group == current.data:
            return True
        elif find_group < current.data:
            current = current.left  # 왼쪽 서브트리로 이동
        else:
            current = current.right  # 오른쪽 서브트리로 이동
    return False  # 값을 찾지 못한 경우

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]  # 트리 삽입할 값들
    root = None  # 트리의 루트 노드는 처음에 None

    # 숫자 리스트를 사용해 트리를 구성
    for group in numbers:
        root = insert(root, group)  # insert 함수로 노드를 트리에 삽입

    print("BST 구성 완료")

    # 특정 값 찾기
    find_group = int(input("찾고 싶은 값을 입력하세요: "))
    if search(root, find_group):
        print(f"{find_group}을(를) 찾았습니다")
    else:
        print(f"{find_group}이(가) 존재하지 않습니다")
