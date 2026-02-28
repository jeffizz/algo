<?php

declare(strict_types=1);

class ArrayTree
{
    public function __construct(public array $tree = [])
    {}

    public function size(): int
    {
        return count($this->tree);
    }

    public function val(int $i): ?int
    {
        if ($i < 0 || $i >= count($this->tree)) {
            return null;
        }
        return $this->tree[$i];
    }

    public function left(int $i): int
    {
        return 2 * $i + 1;
    }

    public function right(int $i): int
    {
        return 2 * $i + 2;
    }

    public function parent(int $i): int
    {
        return floor(($i - 1) / 2);
    }

    public function levelOrderTraverse()
    {
        return $this->tree;
    }

    public function traverse(int $i, array &$arr, int $type = 0)
    {
        if ($this->right($i) >= $this->size()) {
            $arr[] = $this->tree[$i] ?: 'null';
            return ;
        }
        $type == 0 && $arr[] = $this->tree[$i];
        $this->traverse($this->left($i), $arr, $type);
        $type == 1 && $arr[] = $this->tree[$i];
        $this->traverse($this->right($i), $arr, $type);
        $type == 2 && $arr[] = $this->tree[$i];
    }

    public function preOrder()
    {
        $arr = [];
        $this->traverse(0, $arr, 0);
        echo "[" . implode(', ', $arr) . "]\n";
    }

    public function inOrder()
    {
        $arr = [];
        $this->traverse(0, $arr, 1);
        echo "[" . implode(', ', $arr) . "]\n";
    }

    public function postOrder()
    {
        $arr = [];
        $this->traverse(0, $arr, 2);
        echo "[" . implode(', ', $arr) . "]\n";
    }
}

$tree = new ArrayTree([1,2,3,4,5,null,7]);
$tree->preOrder();
$tree->inOrder();
$tree->postOrder();

