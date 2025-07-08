# Network Subnet Analysis Report


## 1. Subnet with Most Hosts

The subnets with the largest capacity are using a /22 subnet mask (255.255.252.0),and each one is providing 1,022 host addresses.

---

## 2. Subnet Overlap

the analysis confirmed that there are -no overlapping subnets- as each subnet occupies a unique address space.

---

## 3. Subnet Size Comparison

Largest Subnets: the /22 subnets offer the largest address space with 1,024 total IPs
Smallest Subnets: the /24 subnets offer the smallest address space with 256 total IPs

---

## 4. IP Allocation Strategy Recommendation

to reduce wasted IPs, implement "Variable Length Subnet Masking (VLSM)"

determine actual host requirements for each segment and re-allocate IP addresses using appropriate sizes subnet masks (for example: /30 for point-to-point links and the /27 for 25 users). This optimizes address usage and saves space for future growth.