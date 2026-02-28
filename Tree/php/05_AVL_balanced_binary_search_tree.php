<?php

declare(strict_types=1);

class TreeNode
{
    public function __construct(
        public int $val = 0,
        public int $height = 0,
        public ?TreeNode $left = null,
        public ?TreeNode $right = null
    ) {}

    public function __toString(): string
    {
        $q = new SplQueue();
        $q->push($this);
        $v = $h = [];
        while($q->count()) {
            $node = $q->shift();
            if (is_null($node)) {
                $v[] = 'null';
                $h[] = 0;
            } else {
                $v[] = $node->val;
                $h[] = $node->height;
                if (!is_null($node->left) || !is_null($node->right)) {
                    $q->push($node->left);
                    $q->push($node->right);
                }
            }
        }
        return "v[" . implode(', ', $v) . "]\n" .
                "h(" . implode(', ', $h) . ")\n-------\n";
    }
}

class AVL
{

    public function __construct(private ?TreeNode $root = null)
    {}

    protected function height(?TreeNode $node)
    {
        return $node === null ? -1 : $node->height;
    }

    protected function updateHeight(?TreeNode $node): void
    {
        $node->height = max(
            self::height($node->left),
            self::height($node->right)
        ) + 1;
    }

    protected function balanceFactor(TreeNode $node): int
    {
        return $node === null ? 0 : self::height($node->left) - self::height($node->right);
    }

    protected function rightRotate(TreeNode $node): TreeNode
    {
        $child = $node->left;
        $subtree = $child->right;
        $child->right = $node;
        $node->left = $subtree;
        self::updateHeight($node);
        self::updateHeight($child);
        return $child;
    }

    protected function leftRotate(TreeNode $node): TreeNode
    {
        $child = $node->right;
        $subtree = $child->left;
        $child->left = $node;
        $node->right = $subtree;
        self::updateHeight($node);
        self::updateHeight($child);
        return $child;
    }

    protected function rotate(TreeNode $node): TreeNode
    {
        $node_balance_factor = self::balanceFactor($node);
        if ($node_balance_factor >= -1 and $node_balance_factor <= 1) return $node;
        if ($node_balance_factor > 1) {
            $child_balance_factor = self::balanceFactor($node->left);
        } else {
            $child_balance_factor = self::balanceFactor($node->right);
        }

        // Right Rotation Only
        if ($node_balance_factor > 1 && $child_balance_factor >= 0) {
            return self::rightRotate($node);
        }

        // Left Rotation Only
        if ($node_balance_factor < -1 && $child_balance_factor <= 0) {
            return self::leftRotate($node);
        }

        // Left then Right
        if ($node_balance_factor > 1 && $child_balance_factor <= 0) {
            $node->left = self::leftRotate($node->left);
            return self::rightRotate($node);
        }

        // Right then Left
        if ($node_balance_factor < -1 && $child_balance_factor >= 0) {
            $node->right = self::rightRotate($node->right);
            return self::leftRotate($node);
        }
    }

    public function insert(int $val): TreeNode
    {
        return $this->root = $this->insertRecursion($this->root, $val);
    }

    public function insertRecursion(?TreeNode $node, int $val): TreeNode
    {
        if ($node === null) {
            return new TreeNode($val);
        }
        if ($node->val == $val) return $node;

        // Recursive Descent
        if ($node->val > $val) {
            $node->left = self::insertRecursion($node->left, $val);
        } else {
            $node->right = self::insertRecursion($node->right, $val);
        }
        // Backtracking
        self::updateHeight($node);
        return self::rotate($node);
    }

    public function remove(int $val): ?TreeNode
    {
        return $this->root = $this->removeRecursion($this->root, $val);
    }

    public function removeRecursion(?TreeNode $node, int $val): ?TreeNode
    {
        if ($node === null)  return null;

        // Recursive Descent
        if ($node->val > $val) {
            $node->left = self::removeRecursion($node->left, $val);
        } elseif ($node->val < $val) {
            $node->right = self::removeRecursion($node->right, $val);
        } else {
            if ($node->left && $node->right) {
                $subtree = $node->left;
                $x = $node->right;
                while ($x->left) {
                    $x = $x->left;
                }
                $x->left = $subtree;
                return $node->right;
            }
            if (!$node->left && !$node->right) {
                return null;
            } else {
                if ($node->left) return $node->left;
                if ($node->right) return $node->right;
            }
        }
        // Backtracking
        self::updateHeight($node);
        return self::rotate($node);
    }

    public function search(TreeNode $root, int $val): TreeNode
    {
        // TODO
    }
}

$avl = new AVL();
echo($avl->insert(6));
echo($avl->insert(4));
echo($avl->insert(2));
echo($avl->insert(8));
echo($avl->insert(10));
echo($avl->remove(2));
echo($avl->insert(5));
echo($avl->remove(10));
echo($avl->insert(7));
echo($avl->remove(5));
