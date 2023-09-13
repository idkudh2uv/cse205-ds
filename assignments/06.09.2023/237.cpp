class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        auto del = node->next;
        node->next = del->next;
        delete(del);
    }
};