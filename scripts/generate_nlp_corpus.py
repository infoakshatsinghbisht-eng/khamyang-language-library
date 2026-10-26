"""
CLI Script to generate Khamyang - English - Hindi - Assamese NLP Training Corpus
================================================================================
Usage:
    python scripts/generate_nlp_corpus.py --count 10000 --shard-size 50000 --output-dir nlp_corpus
    python scripts/generate_nlp_corpus.py --count 500000 --shard-size 50000 --output-dir nlp_corpus
"""

import argparse
import sys
import os
import time

# Ensure workspace root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.stdout.reconfigure(encoding="utf-8")

from khamyang.nlp.corpus_generator import KhamyangNLPGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate Khamyang-English-Hindi-Assamese NLP Training Corpus")
    parser.add_argument("--count", type=int, default=25000, help="Total number of sentences to generate (up to 500,000)")
    parser.add_argument("--shard-size", type=int, default=25000, help="Number of sentences per JSONL shard file")
    parser.add_argument("--output-dir", type=str, default="nlp_corpus", help="Destination output directory (git-ignored)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducible dataset generation")
    args = parser.parse_args()

    start_time = time.time()
    print("=" * 75)
    print("  TAI KHAMYANG - ENGLISH - HINDI NLP TRAINING CORPUS GENERATOR")
    print(f"  Target Volume: {args.count:,} sentences")
    print(f"  Shard Size:    {args.shard_size:,} sentences per file")
    print(f"  Output Dir:    {args.output_dir}/ (Excluded from git)")
    print("=" * 75)

    gen = KhamyangNLPGenerator(seed=args.seed)
    shards = gen.export_sharded_jsonl(
        total_count=args.count,
        output_dir=args.output_dir,
        shard_size=args.shard_size
    )

    elapsed = time.time() - start_time
    print("-" * 75)
    print(f"Generation finished in {elapsed:.2f} seconds ({args.count / max(0.01, elapsed):,.0f} sent/sec).")
    print(f"Total shards generated: {len(shards)}")
    print("=" * 75)

if __name__ == "__main__":
    main()
