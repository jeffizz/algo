<?php

declare(strict_types=1);

class TreeNode {

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

    public static function traverse(?TreeNode $node, int $type = 0): iterable
    {
        if ($node === null) {
            yield 'null';
            return;
        }
        if (!$node->left && !$node->right) {
            yield $node->val;
        } else {
            if ($type === 0) yield $node->val;
            yield from self::traverse($node->left, $type);
            if ($type === 1) yield $node->val;
            yield from self::traverse($node->right, $type);
            if ($type === 2) yield $node->val;
        }

    }
}

$root = TreeNode::buildTree([1, 2, 3, 4, 5, null, 7]);

function printTraversal(string $name, iterable $data): void {
    $result = iterator_to_array($data, false); // false 禁用键名覆盖
    echo "{$name}: [" . implode(', ', $result) . "]\n";
}

printTraversal("PreOrder",  TreeNode::traverse($root, 0));
printTraversal("InOrder",   TreeNode::traverse($root, 1));
printTraversal("PostOrder", TreeNode::traverse($root, 2));
