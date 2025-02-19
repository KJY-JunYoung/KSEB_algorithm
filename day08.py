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

# 트리 삭제 함수
def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # 자식이 없는 노드(리프 노드)
        if root.left is None and root.right is None:
            return None
        # 자식이 하나인 경우
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # 자식이 두 개인 경우
        else:
            # 후속 노드를 찾고, 그 값을 현재 노드로 대체
            root.data = min_value_node(root.right).data
            # 후속 노드를 삭제
            root.right = delete(root.right, root.data)

    return root

# 후속 노드를 찾는 함수 (오른쪽 서브 트리에서 가장 작은 값)
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

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

    # 특정 값 삭제
    delete_value = int(input("삭제할 값을 입력하세요: "))
    root = delete(root, delete_value)
    print(f"{delete_value}을(를) 삭제한 후 BST 구조:")
