import os
import time


queries_folder = "/Users/singh15/Downloads/pre-interview/queries"
cvc5_binary = "/Users/singh15/Downloads/pre-interview/cvc5-macOS-arm64-static-gpl/bin/cvc5"
output_csv = "/Users/singh15/Downloads/pre-interview/results.csv"


# Open CSV file to write results
with open(output_csv, "w") as f:
    f.write("QueryName,Result,ElapsedTime\n")  

    # Process each .smt2 file in the queries folder
    for query in os.listdir(queries_folder):
        if query.endswith(".smt2"): 
            query_path = os.path.join(queries_folder, query)
            start_time = time.time()  

            # Run cvc5
            exit_code = os.system(f"{cvc5_binary} --tlimit=60000 {query_path}")
            elapsed_time = round(time.time() - start_time, 2)  

            # Determine result based on exit code
            if exit_code == 0:
                result = "SAT"
            elif exit_code == 1:
                result = "UNSAT"
            else:
                result = "TIMEOUT"

            # Write result to CSV file and print to console
            f.write(f"{query},{result},{elapsed_time}\n")
            print(f"{query}: {result} ({elapsed_time}s)")

print(f"Results saved to {output_csv}.")
