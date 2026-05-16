import argparse
from modules.hash_verifier import generate_hash
from modules.metadata_analyzer import get_metadata

parser = argparse.ArgumentParser(description="DEAK-WER Forensic Toolkit")

parser.add_argument("--hash", help="Generate hash of file")
parser.add_argument("--meta", help="Extract metadata")

args = parser.parse_args()

if args.hash:
    result = generate_hash(args.hash)
    print("SHA256:", result)

elif args.meta:
    meta = get_metadata(args.meta)
    print(meta)

else:
    print("Use --hash or --meta")


