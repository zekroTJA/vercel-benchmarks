#!/bin/bash

RUNTIMES=(
    "node"
    "go"
    "python"
    "rust"
)

ENDPOINTS=(
    "simple"
)

ROOT="https://verce-test-sand.vercel.app"

OUTPUT="$HOME/vercel-test/results"

COUNT=100
PARALLEL=5
WAIT="1ms..50ms"

# ----------------------------------------------

which rush > /dev/null 2>&1 || {
    echo "error: 'rush' is not installed"
    exit 1
}

for endpoint in ${ENDPOINTS[*]}; do
    for runtime in ${RUNTIMES[*]}; do
        ts=$(date +%Y-%m-%d_%H-%M-%S)
        rush "$ROOT/api/$runtime/$endpoint" \
            --method GET \
            --count $COUNT \
            --parallel $PARALLEL \
            --wait $WAIT \
            --output "$OUTPUT/$endpoint/$runtime/$ts.csv"
    done
done