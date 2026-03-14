<?php

abstract class Heap
{

    public function __construct(protected array $heap = [])
    {
        if (!empty($heap)) {
            $end = count($heap) - 1;
            for ($i = $end; $i >= 0; --$i) {
                $this->siftDown($i);
            }
        }
    }

    public function __toString(): string
    {
        return "[" . implode(", ", $this->heap) . "]\n";
    }

    public function size(): int
    {
        return count($this->heap);
    }

    public function isEmpty(): bool
    {
        return empty($this->heap);
    }

    public function peak(): int
    {
        return $this->heap[0];
    }

    public function push(int $val): Heap
    {
        $this->heap[] = $val;
        $this->siftUp(count($this->heap) - 1);
        return $this;
    }

    public function pop(): Heap
    {
        $end = count($this->heap) - 1;
        $top = $this->peak();
        $this->heap[0] = $this->heap[$end];
        array_pop($this->heap);
        $this->siftDown(0);
        return $this;
    }

    protected function left(int $i): int
    {
        return 2 * $i + 1;
    }

    protected function right(int $i): int
    {
        return 2 * $i + 2;
    }

    protected function parent(int $i): int
    {
        return (int) floor(($i - 1) / 2);
    }

    protected abstract function siftUp(int $i): void;

    protected abstract function siftDown(int $i): void;
}

class MinHeap extends Heap
{

    protected function siftUp(int $i): void
    {
        while (1) {
            $parent = $this->parent($i);
            if ($parent < 0) break;
            if ($this->heap[$parent] > $this->heap[$i]) {
                $tmp = $this->heap[$i];
                $this->heap[$i] = $this->heap[$this->parent($i)];
                $this->heap[$parent] = $tmp;
                $i = $parent;
            } else {
                break;
            }
        }
    }

    protected function siftDown(int $i): void
    {
        $end = $this->size() - 1;
        while (1) {
            $left = $this->left($i);
            $right = $this->right($i);
            if ($left > $end) break;
            if ($left == $end || $this->heap[$left] <= $this->heap[$right]) {
                if ($this->heap[$i] >= $this->heap[$left]) {
                    $tmp = $this->heap[$i];
                    $this->heap[$i] = $this->heap[$left];
                    $this->heap[$left] = $tmp;
                    $i = $left;
                } else {
                    break;
                }
            } else {
                if ($this->heap[$i] >= $this->heap[$right]) {
                    $tmp = $this->heap[$i];
                    $this->heap[$i] = $this->heap[$right];
                    $this->heap[$right] = $tmp;
                    $i = $right;
                } else {
                    break;
                }
            }
        }
    }
}


class TopK
{
    protected MinHeap $heap;

    public function __construct(int $k, array $init = [])
    {
        $count = count($init);
        if ($count <= $k) {
            $this->heap = new MinHeap($init);
        } else {
            $this->heap = new MinHeap();
            for ($i = 0; $i < $k; ++$i) {
                $this->heap->push($init[$i]);
            }
            while ($k < $count) {
                $this->consume($init[$k]);
                ++$k;
            }
        }
    }

    public function __toString(): string
    {
        return $this->heap->__toString();
    }

    public function consume(int $val): TopK
    {
        if ($val > $this->heap->peak()) {
            $this->heap->pop();
            $this->heap->push($val);
        }
        return $this;
    }
}


$heap = new MinHeap([25, 9, 3, 30, 7, 2, 14]);
echo ($heap);
echo ($heap->pop());

$topk = new TopK(3, [25, 9, 3, 30, 7, 2, 14]);
echo ($topk);
echo ($topk->consume(90));
echo ($topk->consume(120));
echo ($topk->consume(18));
