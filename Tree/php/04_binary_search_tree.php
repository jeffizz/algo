<?php

declare(strict_types=1);

class TreeNode
{

    public function __construct(
        public int $val = 0,
        public ?TreeNode $left = null,
        public ?TreeNode $right = null
    ) {}

    public function __toString(): string
    {
        $q = new SplQueue();
        $q->push($this);
        $arr = [];
        while($q->count()) {
            $node = $q->shift();
            if (is_null($node)) {
                $arr[] = 'null';
            } else {
                $arr[] = $node->val;
                if (!is_null($node->left) || !is_null($node->right)) {
                    $q->push($node->left);
                    $q->push($node->right);
                }
            }
        }
        return "[" . implode(', ', $arr) . "]\n";
    }
}


class BST {

    public function __construct(private ?TreeNode $root = null)
    {}

    public function __toString()
    {
        return $this->root ? $this->root->__toString() : '';
    }

    public function search(int $val): ?TreeNode
    {
        $cur = $this->root;
        while($cur) {
            if ($cur->val == $val) {
                return $cur;
            }
            if ($cur->val > $val) {
                $cur = $cur->left;
            } else {
                $cur = $cur->right;
            }
        }
        return null;
    }

    public function insert(int $val): BST
    {
        if ($this->root === null) {
            $this->root = new TreeNode($val);
            return $this;
        }
        list($cur, $pre) = [$this->root, null];
        while($cur) {
            if ($cur->val == $val) {
                return $this->root;
            }
            if ($cur->val > $val) {
                $pre = $cur;
                $cur = $cur->left;
            } else {
                $pre = $cur;
                $cur = $cur->right;
            }
        }
        if ($pre->val > $val) {
            $pre->left = new TreeNode($val);
        } else {
            $pre->right = new TreeNode($val);
        }
        return $this;
    }

    public function remove(int $val): BST
    {
        list($cur, $pre) = [$this->root, null];
        while($cur) {
            if ($cur->val == $val) {
                break;
            }
            if ($cur->val > $val) {
                $pre = $cur;
                $cur = $cur->left;
            } else {
                $pre = $cur;
                $cur = $cur->right;
            }
        }

        if ($cur === null) {
            return $this;
        }

        if ($pre === null) {
            if (!$cur->left) {
                $this->root = $cur->right;
                return $this;
            }
            if (!$cur->right) {
                $this->root = $cur->left;
                return $this;
            }
        }

        if (!$cur->left) {
            if ($pre->val > $cur->val) {
                $pre->left = $cur->right;
            } else {
                $pre->right = $cur->right;
            }
            return $this;
        }

        if (!$cur->right) {
            if ($pre->val > $cur->val) {
                $pre->left = $cur->left;
            } else {
                $pre->right = $cur->left;
            }
            return $this;
        }

        // node replacement instead of subtree attachment
        $tmp = $cur->right;
        while ($tmp->left) {
            $tmp = $tmp->left;
        }
        $this->remove($tmp->val);
        $cur->val = $tmp->val;
        return $this;
    }

    public function traversal(?TreeNode $root, array &$arr, int $style = 0)
    {
        if ($root === null) {
            return ;
        }
        if ($root->left === null && $root->right === null) {
            $arr[] = $root->val;
            return ;
        }
        $style == 0 && $arr[] = $root->val;
        $this->traversal($root->left, $arr, $style);
        $style == 1 && $arr[] = $root->val;
        $this->traversal($root->right, $arr, $style);
        $style == 2 && $arr[] = $root->val;
    }

    public function inOrder()
    {
        $arr = [];
        $this->traversal($this->root, $arr, 1);
        return "[" . implode(', ', $arr) . "]\n";
    }
}

$bst = new BST();

echo(
    $bst->insert(8)->insert(4)->insert(12)->insert(2)->insert(6)->insert(10)
        ->insert(14)->insert(1)->insert(3)->insert(5)->insert(7)->insert(9)
        ->insert(11)->insert(13)->insert(15)
);
echo($bst->search(14));
echo($bst->remove(15));
echo($bst->remove(14));
echo($bst->remove(12));
echo($bst->search(13));
echo($bst->remove(8));
echo("inOrder: " . $bst->inOrder());
echo($bst->search(13));
echo($bst->insert(8));
