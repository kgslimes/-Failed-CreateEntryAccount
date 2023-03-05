login = "\n    mutation (\n        $username: String!, \n        $password: String!, \n        $rememberme: Boolean, \n        $captchaValue: String, \n        $captchaKey: String,\n        $captchaType: String\n    ) {\n        signinByUsername (\n            username: $username, \n            password: $password, \n            rememberme: $rememberme, \n            captchaValue: $captchaValue, \n            captchaKey: $captchaKey,\n            captchaType: $captchaType\n        ) {\n            \n    id\n    username\n    nickname\n    role\n    isEmailAuth\n    isSnsAuth\n    isPhoneAuth\n    studentTerm\n    alarmDisabled\n    status {\n        userStatus\n    }\n    profileImage {\n        \n    id\n    name\n    label {\n        \n    ko\n    en\n    ja\n    vn\n\n    }\n    filename\n    imageType\n    dimension {\n        \n    width\n    height\n\n    }\n    trimmed {\n        filename\n        width\n        height\n    }\n\n    }\n    banned {\n        username\n        nickname\n        reason\n        bannedCount\n        bannedType\n        projectId\n        startDate\n        userReflect {\n            status\n            endDate\n        }\n    }\n    isProfileBlocked\n\n        }\n    }\n"

query = "\n    query ($type: String, $word: String) {\n        prohibitedWord(type: $type, word: $word) {\n            \n    status\n    result\n\n        }\n    }\n"

create = "\n    mutation (\n        $role: String!,\n        $grade: String!,\n        $gender: String!,\n        $nickname: String!,\n        $email: String,\n        $username: String!,\n        $password: String!,\n        $passwordConfirm: String!,\n        $mobileKey: String,\n        $signupToken: String,\n    ) {\n        signupByUsername(\n            role: $role,\n            grade: $grade ,\n            gender: $gender ,\n            nickname: $nickname ,\n            email: $email ,\n            username: $username ,\n            password: $password,\n            passwordConfirm: $passwordConfirm,\n            mobileKey: $mobileKey,\n            signupToken: $signupToken,\n        ) {\n            \n    id\n    username\n    nickname\n    role\n    isEmailAuth\n    isSnsAuth\n    isPhoneAuth\n    studentTerm\n    alarmDisabled\n    status {\n        userStatus\n    }\n    profileImage {\n        \n    id\n    name\n    label {\n        \n    ko\n    en\n    ja\n    vn\n\n    }\n    filename\n    imageType\n    dimension {\n        \n    width\n    height\n\n    }\n    trimmed {\n        filename\n        width\n        height\n    }\n\n    }\n    banned {\n        username\n        nickname\n        reason\n        bannedCount\n        bannedType\n        projectId\n        startDate\n        userReflect {\n            status\n            endDate\n        }\n    }\n    isProfileBlocked\n\n        }\n    }\n"
