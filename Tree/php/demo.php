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

    public static function buildTree(array $arr): TreeNode|null
    {
        if(!$total = count($arr)) {
            return null;
        }
        $i = 1;
        $root = new TreeNode($arr[0]);
        $q = new SplQueue();
        $q->push($root);
        while($q->count()) {
            $node = $q->shift();
            if ($i < $total && $arr[$i]) {
                $node->left = new TreeNode($arr[$i]);
                $q->push($node->left);
            }
            ++$i;
            if ($i < $total && $arr[$i]) {
                $node->right = new TreeNode($arr[$i]);
                $q->push($node->right);
            }
            ++$i;
        }
        return $root;
    }
}

$arr = [1, 2, null, null, 3, 4, 5, null, 6];
echo(TreeNode::buildTree($arr));

