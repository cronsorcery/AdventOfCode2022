# Find n of trees whose value is -gt than
# any of the trees left, right, above and below
$Grid = Get-Content .\input.txt

function isVisible {
    param (
        [int]$tree,
        [Object[]]$array
    )
    ($array | Measure-Object -Maximum).Maximum -lt $tree
}

function calculateScenicScore {
    param (
        [int]$tree,
        [Object[]]$_above,
        [Object[]]$_below,
        [Object[]]$_before,
        [Object[]]$_after
    )
    # reverse order: above,before
    $_above = $_above[($above.Length-1)..0]
    $_before = $_before[($before.Length-1)..0]

    $viewingDistance = $_above,$_below,$_before,$_after | ForEach-Object {
        $visibleFromTreeCount = 0
        for ($i=0; $i -lt $_.Length; ++$i) {
            if ($_[$i] -lt $tree) {
                $visibleFromTreeCount++
            } else {
                $visibleFromTreeCount++
                break
            }
        }
        if ($visibleFromTreeCount -gt 0) {
            $visibleFromTreeCount
        }
    }
    $viewingDistance | ForEach-Object {$total=1} {$total *= $_} {$total}
}

Invoke-Command {
    # Count trees facing the outer side
    $VisibleTreeCount = ($Grid[0].Length * 2) + ($Grid[1..($Grid.Count-2)].Count * 2)
    $MaxScenicScore = 0

    # Count the rest of the trees
    for ($i = 1; $i -lt $Grid.Count-1; ++$i) {
        $CurrentRow = $Grid[$i].ToCharArray() | ForEach-Object {[System.Int32]::Parse($_)}
        for ($j = 1; $j -lt $CurrentRow.Count-1; ++$j) {
            $CurrentTree = [System.Int32]::Parse($CurrentRow[$j])
            $before =  $CurrentRow[0..($j-1)]
            $after  = $CurrentRow[($j+1)..$CurrentRow.GetUpperBound(0)]
            $above  = $Grid[0..($i-1)] | ForEach-Object {$k=0} {[system.Int32]::Parse($_[$j])}
            $below  = $Grid[($i+1)..$Grid.GetUpperBound(0)] | ForEach-Object {$k=0} {[system.Int32]::Parse($_[$j])}

            if ($(isVisible -tree $CurrentTree -array $above)) {
                $VisibleTreeCount++
            } elseif ($(isVisible -tree $CurrentTree -array $below)) {
                $VisibleTreeCount++
            } elseif ($(isVisible -tree $CurrentTree -array $before)) {
                $VisibleTreeCount++
            } elseif ($(isVisible -tree $CurrentTree -array $after)) {
                $VisibleTreeCount++
            }

            $CurrentScenicScore = calculateScenicScore $CurrentTree $above $below $before $after
            if ($CurrentScenicScore -gt $MaxScenicScore) {
                $MaxScenicScore = $CurrentScenicScore
            }
        }
    }

    "Visible trees: {0}" -f $VisibleTreeCount
    "Max scenic score: {0}" -f $MaxScenicScore
}
