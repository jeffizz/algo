<?php

class MaxHeap
{
    public function __construct(private array $heap = [])
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

    public function push(int $val): MaxHeap
    {
        $this->heap[] = $val;
        $this->siftUp(count($this->heap) - 1);
        return $this;
    }

    public function pop(): MaxHeap
    {
        $end = count($this->heap) - 1;
        $top = $this->peak();
        $this->heap[0] = $this->heap[$end];
        array_pop($this->heap);
        $this->siftDown(0);
        return $this;
    }

    private function left(int $i): int
    {
        return 2 * $i + 1;
    }

    private function right(int $i): int
    {
        return 2 * $i + 2;
    }

    private function parent(int $i): int
    {
        return (int) floor(($i - 1) / 2);
    }

    private function siftUp(int $i): void
    {
        while (1) {
            $parent = $this->parent($i);
            if ($parent < 0) break;
            if ($this->heap[$parent] < $this->heap[$i]) {
                $tmp = $this->heap[$i];
                $this->heap[$i] = $this->heap[$this->parent($i)];
                $this->heap[$parent] = $tmp;
                $i = $parent;
            } else {
                break;
            }
        }
    }

    private function siftDown(int $i): void
    {
        $end = $this->size() - 1;
        while (1) {
            $left = $this->left($i);
            $right = $this->right($i);
            if ($left > $end) break;
            if ($left == $end || $this->heap[$left] >= $this->heap[$right]) {
                if ($this->heap[$i] <= $this->heap[$left]) {
                    $tmp = $this->heap[$i];
                    $this->heap[$i] = $this->heap[$left];
                    $this->heap[$left] = $tmp;
                    $i = $left;
                } else {
                    break;
                }
            } else {
                if ($this->heap[$i] <= $this->heap[$right]) {
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

// Create and Matipulate a Max Heap by pushing and popping values
$heap = new MaxHeap();
echo ($heap->push(7));
echo ($heap->push(14));
echo ($heap->push(25));
echo ($heap->push(3));
echo ($heap->push(9));
echo ($heap->push(30));
echo ($heap->push(2));
echo ($heap->pop());
echo ($heap->pop());
echo ($heap->pop());

// Create a Max Heap from an array of values
echo (new MaxHeap([2, 3, 7, 9, 14, 25, 30]));

