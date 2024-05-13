# Design FAQs

**Q: Protobuf and Python circularity code-smell: it seems that the flow of the application is designed with a circular, potentially redundant structure. The implementer configures the data model by using the PBobject-generating python scripts, but any PBobject is wrapped in Python classes when it is used in a Python-implemented component of the application. Can we still justify this design?**

*A: This type of situation does arise in systems where you're trying to bridge the gap between user-friendly configuration and system-level serialization requirements, especially when aiming for cross-language compatibility and strict type consistency. Here’s a breakdown to clarify the roles and justify the structure:*

### Purpose of Each Component:

#### 1. **Protobuf Classes**:
- **Primary Role**: Define a language-neutral, serialization-friendly structure for data that can be easily transmitted, stored, or used across different programming environments.
- **System Integration**: Ensure data integrity and uniformity across various parts of a distributed system or across applications written in different languages.

#### 2. **Python Wrapper for PB Classes**:
- **Primary Role**: Provide a more intuitive, Pythonic interface to the PB classes. This includes methods for easier handling of data, additional functionality (like validation or transformation), and integration with Python-specific features.
- **Developer Experience**: Improve usability and readability for developers working within the Python ecosystem, abstracting away some of the verbosity or complexity of direct protobuf manipulation.

#### 3. **PB Wrapper Functions in Python (`create_feature`, `create_solver_type`)**:
- **Primary Role**: Simplify the creation of PB objects from Python, particularly for configurations or definitions that are more naturally expressed in a high-level script. This includes setting up complex objects without directly dealing with all protobuf details.
- **Implementer Interface**: Allow implementers who may not be familiar with protobuf specifics to define necessary components in a straightforward manner. It acts as a bridge between high-level concepts and their protobuf representations.

### Analyzing the Design: Is It Circular or Just Layered?

While it might seem that the design is circular—Python creating protobufs and protobufs being wrapped in Python—it is actually a layered approach:

- **Layer 1 (Python Configuration Layer)**: Where the implementers interact, defining features and solver types using friendly Python functions.
- **Layer 2 (Protobuf Layer)**: The core data structure layer that handles serialization and cross-language compatibility.
- **Layer 3 (Python Wrapping Layer)**: Adds additional functionality and ease of use to the raw protobuf objects, making them more accessible and functional within Python codebases.

### Justification and Potential Revisions

- **Justification**: This design ensures flexibility and usability while maintaining the robustness and cross-language capabilities provided by protobufs. It separates concerns by distinguishing between configuration, data structuring, and functional interfacing.
- **Potential Revisions**: Consider whether:
    - **Integration Tightness**: Could the layers be more tightly integrated? For instance, could the Python wrappers generate PB objects directly, skipping the PB wrapper functions?
    - **Abstraction Level**: Is there an intermediate layer that could be removed or combined? Perhaps the PB wrapper functions could be part of the Python wrappers, making them more directly responsible for generating their PB counterparts.

### Conclusion

The system design makes sense when considering the need for both easy configurability by implementers (who might not be proto-savvy) and robust data handling across different system parts or languages. However, always be open to revisiting the architecture as the system evolves or as more insights are gained during development. If a particular layer becomes too cumbersome or redundant, it might be a sign to simplify or reorganize the responsibilities.
