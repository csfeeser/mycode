```mermaid
graph TD
    subgraph Kubernetes_Basics "Kubernetes Basics"
        A[What is/why use Kubernetes?] --> B[Kubernetes Architecture]
        B --> C[Control Plane Components]
        C --> D[Creating container images from Dockerfile]
        D --> E[What are containers?]
    end

    subgraph YAML_and_API "YAML and API"
        F[YAML] --> G[Writing Manifests]
        G --> H[Creating Pods]
        H --> I[kubectl get/describe API]
        I --> J[Versioning/Deprecations]
    end

    subgraph Cluster_Organization "Cluster Organization"
        AU["Namespaces"]
    end

    subgraph Debugging_Tools "Debugging Tools"
        AP["kubectl port-forward"] --> AQ["kubectl exec"]
    end

    subgraph Monitoring "Monitoring"
        AT["Readiness and Liveness Probes"]
    end

    subgraph Logging "Logging"
        S[Container logging] --> T[kubectl logs]
        T --> U[3rd Party Logging]
    end

    subgraph Container_Lifecycle "Container Lifecycle"
        AB[Sidecar Containers] --> AC[Init Containers]
    end

    subgraph Resource_Management "Resource Management"
        K[Limits vs. Requests] --> L[ResourceQuotas]
        L --> M[LimitRanges]
        M --> N[kubectl top]
    end

    subgraph Storage_Basics "Storage Basics"
        V[Volume Mounting] --> W[Configmaps]
        W --> X[Secrets]
    end

    subgraph Advanced_Storage "Advanced Storage"
        Y[Persistent Volumes & Persistent Volume Claims] --> Z[Storage Classes]
        Z --> AA[CSI Storage]
    end

    subgraph Workloads "Workloads"
        AD[Labels & Selectors] --> AE[Annotations]
        AE --> AF[ReplicaSets]
        AF --> AG[DaemonSets]
        AG --> AH[Deployments]
        AH --> AI[Manual vs. AutoScaling with Horizontal Pod Autoscaler]
    end

    subgraph Job_Scheduling "Job Scheduling"
        AJ[Jobs] --> AK[Cronjobs]
    end

    subgraph Access_Control "Access Control"
        O[Roles & RoleBindings] --> P[ClusterRoles & ClusterRoleBindings]
        P --> Q[ServiceAccounts]
        Q --> R[Contexts]
    end

    subgraph Networking "Networking"
        AL[Services- ClusterIP, NodePort, LoadBalancer] --> AM[NetworkPolicies]
        AM --> AN[Ingress & Ingress Controllers]
        AN --> AO[Networking Plugins- Calico]
    end

    subgraph Node_Access_Control "Node Access Control"
        AV["Taints and Tolerations"]
    end

    subgraph Extension_Tools "Extension Tools"
        AR[Helm] --> AS[CRD - Custom Resource Definitions]
    end

    Kubernetes_Basics --> YAML_and_API
    YAML_and_API --> Cluster_Organization
    Cluster_Organization --> Debugging_Tools
    Cluster_Organization --> Resource_Management
    Cluster_Organization --> Workloads
    Debugging_Tools --> Monitoring
    Monitoring --> Logging
    Logging --> Container_Lifecycle
    Resource_Management --> Storage_Basics
    Storage_Basics --> Advanced_Storage
    Workloads --> Job_Scheduling
    Job_Scheduling --> Access_Control
    Access_Control --> Networking
    Access_Control --> Node_Access_Control
    Networking --> Extension_Tools
    Node_Access_Control --> Extension_Tools
    Advanced_Storage --> Extension_Tools
    Container_Lifecycle --> Extension_Tools
    Extension_Tools --> Pass_CKAD_Exam["Pass the CKAD Exam!"]
```
