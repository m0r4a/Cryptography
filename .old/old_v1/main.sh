#!/bin/bash


select algorithm in "cesar" "euclidean" "diophantine"; do
    case $algorithm in
        "cesar")
	    algorithm="cesar.py"
            break
            ;;
        "euclidean")
	    algorithm="euclidean.py"
            break
            ;;
        "diophantine")
	    algorithm="diophantine.py"
            break
            ;;
        *)
            echo "Please, select a valid option"
            ;;
    esac
done

python3 algorithms/$algorithm
