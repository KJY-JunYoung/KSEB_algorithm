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
            return current
        elif find_group < current.data:
            current = current.left  # 왼쪽 서브트리로 이동
        else:
            current = current.right  # 오른쪽 서브트리로 이동
    return None  # 값을 찾지 못한 경우

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

# 후속 노드를 찾는 함수
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

if __name__ == "__main__":
    root = None
    while True:
        print("\n--- 트리 관리 메뉴 ---")
        print("1. 값 삽입")
        print("2. 값 삭제")
        print("3. 값 찾기")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':  # 값 삽입
            value = int(input("삽입할 값을 입력하세요: "))
            root = insert(root, value)
            print(f"{value} 삽입 완료")

        elif choice == '2':  # 값 삭제
            value = int(input("삭제할 값을 입력하세요: "))
            if search(root, value):
                root = delete(root, value)
                print(f"{value} 삭제 완료")
            else:
                print(f"{value}은(는) 트리에 존재하지 않습니다.")

        elif choice == '3':  # 값 찾기
            value = int(input("찾고 싶은 값을 입력하세요: "))
            if search(root, value):
                print(f"{value}을(를) 찾았습니다.")
            else:
                print(f"{value}이(가) 존재하지 않습니다.")

        elif choice == '4':  # 종료
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 선택하세요.")
